from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Item, ItemImage, Category, Label 
from .forms import ItemForm, CheckoutForm

# Create your views here.


class SearchListView(ListView):
    paginate_by = 15
    template_name = "main/search.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Item.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        # return super().get_queryset()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get('q') 
        return context
    

# class SearchListView(TemplateView):

#     def get(self, request):
#         template_name = "main/search_list.html"
#         try:
#             query = request.Get.get('q')
#             object_list = Item.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
#             context = {"search_result": object_list, "query":query}
#         except expression as identifier:
#             context = {"search_result": "Sorry", "query":query}
#         return render(request, template_name, context)


class HomeListView(ListView):
    model = Item
    template_name = "main/index.html"


class ItemListView(ListView):
    model = Item
    paginate_by = 12
    # template_name = ".html"


class ItemDetailView(DetailView):
    model = Item
    # template_name = ".html"


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    # template_name = ".html"


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    # template_name = ".html"


class ItemDeleteView(DeleteView):
    model = Item
    # template_name = ".html"




