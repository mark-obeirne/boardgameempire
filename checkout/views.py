from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from cart.contexts import cart_contents
import stripe
from django.conf import settings


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is currently empty")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart["grand_total"]
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            "Did you forget to set your Stripe public key in your environment?")

    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51HieJBFDbEFsB8WkeMbtU3A1VOoXZiLUDK1R8dZNKmAIaLzLurFz2UR46wQe8NSSJlil7RlmTWpZZNCf8jKqb8wN00bhnWedj1",
        "client_secret": "intent.client_secret",
    }
    return render(request, "checkout/checkout.html", context)
