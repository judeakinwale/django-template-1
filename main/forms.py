from django import forms
from .models import Item
# from django_countries.fields import CountryField
# from django_countries.fields import CountrySelectWidget


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal')
)


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ["title", "description", "category", "label", "price", "sale_price", "start_time", "end_time", "image", "slug"]
