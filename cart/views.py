from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.views.generic import ListView, TemplateView, View
from .models import OrderItem, Order, BillingAddress, Payment 
from main.models import Item

# Create your views here.


class OrderListView(ListView):
    template_name = "cart/cart.html"

    def get_queryset(self, *args, **kwargs):
        try:
            object_list = Order.objects.get(user=self.request.user, ordered=False)
            
        except:
            object_list = None
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            # self.get_context_data
            self.get_queryset()
            context["message"] = "My cart"
        except:
            messages.error(request, "Your do not have an active order")
            context["message"] = "Your cart is empty"
        return context
    

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    try:
        order_queryset = Order.objects.filter(user=request.user, ordered=False)
        order = order_queryset[0]
        try:
            order.items.filter(item__slug=slug)
            order_item.quantity += 1
            order_item.save()
            order.items.add(order_item)
            messages.info(request, 'This item quantity was updated')
            return redirect("cart:cart")
        except:
            order.items.add(order_item)
            # order.items.save()
            messages.info(request, 'This item was added to your cart')
            return redirect("cart:cart")
    except:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'This item was added to your cart')
        return redirect("cart:cart")


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)
    try:
        order_queryset = Order.objects.filter(user=request.user, ordered=False)
        order = order_queryset[0]
        try:
            order.items.filter(item__slug=slug)
            order.items.remove(order_item[0])
            messages.info(request, 'This item was removed from your cart')
            return redirect("cart:cart")
        except:
            messages.info(request, 'This item was not in your cart')
            return redirect("cart:cart")
    except:
        messages.error(request, 'You do not have an active order')
        return redirect("cart:cart")


def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)
    try:
        order_queryset = Order.objects.filter(user=request.user, ordered=False)
        order = order_queryset[0]
        try:
            order.items.filter(item__slug=slug)
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, 'This item quantity was updated')
            else:
                order.items.remove(order_item[0])
                messages.info(request, 'This item was removed from your cart')
            return redirect("cart:cart")
        except:
            messages.info(request, 'This item was not in your cart')
            return redirect("cart:cart")
    except:
        messages.error(request, 'You do not have an active order')
        return redirect("cart:cart")


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {'form':form}
        return render(self.request, 'cart/checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                # print(form.cleaned_data)
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                # country = form.cleaned_data.get('country')
                zipcode = form.cleaned_data.get('zipcode')
                # TODO: add functionaliity for these fields
                # same_shipping_address = form.cleaned_data.get(
                #     'same_shipping_address')
                # save_info = form.cleaned_data.get('save_info')
                payment_method = form.cleaned_data.get('payment_method')
                billing_address = BillingAddress(
                    user=self.request.user,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zipcode=zipcode,
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()

                if payment_method == 'S':
                    return redirect("products:payment", payment_method='stripe')
                elif payment_method == 'P':
                    return redirect("products:payment", payment_method='paypal')
                else:
                    messages.warning(self.request, 'Invalid payment option selected')
                    return redirect("products:checkout")

            messages.warning(self.request, 'Failed checkout')
            return redirect("cart:checkout")
            
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("cart:cart")