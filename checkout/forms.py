from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("full_name", "email", "street_address1", "street_address2", "town_or_city", "county_or_state", "postcode", "country", "billing_full_name", "billing_street_address1", "billing_street_address2", "billing_town_or_city", "billing_county_or_state", "billing_country", "gift_purchase")

        def __init__(self, *args, **kwargs):
            """ 
            Add placeholders and classes, remove auto-generated labels, and set focus
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                "full_name": "Full Name",
                "email": "Email Address",
                "street_address1": "Street Address 1",
                "street_address2": "Street Address 2",
                "town_or_city": "Town or City",
                "county_or_state": "County or State",
                "postcode": "Postcode",
                "country": "Country",
                "billing_full_name": "Full Name",
                "billing_street_address1": "Street Address 1",
                "billing_street_address2": "Street Address 2",
                "billing_town_or_city": "Town or City",
                "billing_county_or_state": "County or State",
                "billing_country": "Country",
            }

            self.fields["full_name"].widget.attrs["autofocus"] = True

            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
                self.fields[field].widget.attrs["class"] = "stripe-style-input"
                self.fields[field].label = False
