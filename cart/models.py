from django.db import models
from django.contrib.auth.models import User
from main.models import Item

# Create your models here.


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_item_sale_price(self):
        return self.quantity * self.item.sale_price

    def get_amount_saved(self):
        return self.get_total_item_price - self.get_total_item_sale_price

    def get_final_price(self):
        if self.item.sale_price:
            return self.get_total_item_sale_price()
        return self.get_total_item_price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField("OrderItem")
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey("BillingAddress", on_delete=models.CASCADE, null=True, blank=True)
    payment = models.ForeignKey("Payment", on_delete=models.CASCADE, null=True, blank=True)
    

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.request.user.username

    def get_total(self):
        total = 0
        for item in self.items.all():
            total += item.get_final_price()
        return total


class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    street_address = models.CharField(max_length=150)
    apartment_address = models.CharField(max_length=150, null=True, blank=True)
    #TODO 
    #Add state and a better country
    # state = models.CharField(max_length=150, null=True, blank=True)
    #country = CountryField(multiple=False)
    zipcode = models.CharField(max_length=150, null=True, blank=True)
    

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return request.user.username


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    charge_id = models.CharField(max_length=150)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return self.request.user.username

