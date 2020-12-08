from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product

import json
import time


class StripeWH_Handler:
    """ Handle Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle generic / unknown / unexpected webhook events """
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle Stripe's payment_intent.succeeded webhook """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        print(cart)
        billing_details = intent.charges.data[0].billing_details
        print(billing_details)
        print(type(billing_details))
        shipping_details = intent.shipping
        print(shipping_details)
        grand_total = round(intent.charges.data[0].amount / 100, 2)
        print(grand_total)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            print(attempt)
            try:
                order = Order.objects.get(
                    billing_full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    billing_town_or_city__iexact=billing_details.address.city,
                    billing_street_address1__iexact=billing_details.address.line1,
                    billing_street_address2__iexact=billing_details.address.line2,
                    billing_county_or_state__iexact=billing_details.address.state,
                    billing_country__iexact=billing_details.address.country,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                    full_name__iexact=shipping_details.name,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county_or_state__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            print("order exists")
            return HttpResponse(content=f"Webhook received: {event['type']} | SUCCESS: Order exists in the database", status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    billing_full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    billing_town_or_city__iexact=billing_details.address.city,
                    billing_street_address1__iexact=billing_details.address.line1,
                    billing_street_address2__iexact=billing_details.address.line2,
                    billing_county_or_state__iexact=billing_details.address.state,
                    billing_country__iexact=billing_details.address.country,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                    full_name__iexact=shipping_details.name,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county_or_state__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                )
                for product_id, quantity in json.loads(bag).items():
                    product = Product.objects.get(id=product_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                    return HttpResponse(content=f"Webhook received: {event['type']} | ERROR: {e}", status=500)

        return HttpResponse(
            content=f"Webhook received: {event['type']} | SUCCESS: Created order in webhook",
            status=200
        )

    def handle_payment_intent_failed(self, event):
        """ Handle Stripe's payment_intent.payment_failed webhook """
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200
        )
