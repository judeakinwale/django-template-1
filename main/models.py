from django.db import models
from django.shortcuts import reverse, redirect

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    label = models.ForeignKey("Label",on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    image = models.ImageField(upload_to="main/static/items/img", default="main/static/items/img/defalt.jpg", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    slug = models.SlugField(unique=True)
    #TODO: Add location
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.title

    def get_price(self):
        if self.sale_price:
            return self.sale_price
        return self.price

    def get_absolute_url(self):
        return reverse("main:item_detail", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("main:add_to_cart", kwargs={"slug": self.slug})
    
    def get_remove_form_cart_url(self):
        return reverse("main:remove_from_cart", kwargs={"slug": self.slug})


class ItemImage(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="main/static/items/img", default="main/static/items/img/defalt.jpg", height_field=None, width_field=None, max_length=None)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"

    def __str__(self):
        return self.item.title


class Category(models.Model):
    name = models.CharField(max_length=150)
    summary = models.CharField(max_length=250)
    slug = models.CharField(max_length=150)
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Label(models.Model):
    name = models.CharField(max_length=150)
    summary = models.CharField(max_length=250)
    slug = models.CharField(max_length=150)
    

    class Meta:
        verbose_name = "Label"
        verbose_name_plural = "Labels"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("label_detail", kwargs={"slug": self.slug})