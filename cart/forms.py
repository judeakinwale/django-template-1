from django import forms


class CheckoutForm(forms.Form):
    street_address = forms.CharField(required=False)
    apartment_address = forms.CharField(required=False)
    # country = CountryField(required=False, blank_label="Select Country").formfield(widget=CountrySelectWidget())
    zipcode = forms.CharField(required=False)
    # same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_method = forms.ChoiceField(widget=forms.RadioSelect(), choices=[PAYMENT_CHOICES], required=False)