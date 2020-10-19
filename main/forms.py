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


class CheckoutForm(forms.Form):
    street_address = forms.CharField(required=False)
    apartment_address = forms.CharField(required=False)
    # country = CountryField(required=False, blank_label="Select Country").formfield(widget=CountrySelectWidget())
    zipcode = forms.CharField(required=False)
    # same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_method = forms.ChoiceField(widget=forms.RadioSelect(), choices=[PAYMENT_CHOICES], required=False)

