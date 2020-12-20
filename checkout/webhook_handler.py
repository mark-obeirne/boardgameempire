from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time
from math import ceil


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
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)

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
            self._send_order_confirmation_email(order)
            self._update_product_inventory(order, cart)
            self._update_product_quantity_sold(order, cart)
            return HttpResponse(content=f"Webhook received: {event['type']} | SUCCESS: Order exists in the database", status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    user_profile=profile,
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
                for product_id, quantity in json.loads(cart).items():
                    product = Product.objects.get(id=product_id)
                    if profile:
                        lineitem_points_earned = ceil((product.price * quantity) * 10)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            lineitem_points_earned=lineitem_points_earned,
                        )
                        profile.loyalty_points += lineitem_points_earned
                        profile.save()
                    else:
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

        self._send_order_confirmation_email(order)
        self._update_product_inventory(order, cart)
        self._update_product_quantity_sold(order, cart)
        return HttpResponse(
            content=f"Webhook received: {event['type']} | SUCCESS: Created order in webhook",
            status=200
        )

    def _send_order_confirmation_email(self, order):
        """ Send customer a confirmation email once order is created """
        cust_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order}
        )
        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def _update_product_inventory(self, order, cart):
        """ Update product's inventory based on quantity sold """
        for product_id, quantity in json.loads(cart).items():
            product = Product.objects.get(id=product_id)
            product.inventory -= quantity
            product.save()

    def _update_product_quantity_sold(self, order, cart):
        """ Update product's overall quantity sold based on quantity sold in transaction """
        for product_id, quantity in json.loads(cart).items():
            product = Product.objects.get(id=product_id)
            product.quantity_sold += quantity
            product.save()

    def handle_payment_intent_failed(self, event):
        """ Handle Stripe's payment_intent.payment_failed webhook """
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200
        )
