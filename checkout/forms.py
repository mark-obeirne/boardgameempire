from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "street_address1",
            "street_address2",
            "town_or_city",
            "county_or_state",
            "postcode",
            "country",
            "billing_full_name",
            "billing_street_address1",
            "billing_street_address2",
            "billing_town_or_city",
            "billing_county_or_state",
            "billing_country",
            "gift_purchase",
            "points_used"
            )

    def __init__(self, *args, **kwargs):
        """
        Set autofocus, and classes to apply to fields
        """
        super().__init__(*args, **kwargs)

        self.fields["full_name"].widget.attrs["autofocus"] = True

        delivery_fields = [
            "full_name", "email",
            "street_address1", "street_address2",
            "town_or_city", "county_or_state",
            "postcode", "country"
            ]

        for field in self.fields:
            if field in delivery_fields:
                self.fields[field].widget.attrs[
                    'class'] = 'stripe-style-input delivery-input-field'
            else:
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
