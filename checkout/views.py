from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is currently empty")
        return redirect(reverse('products'))
    order_form = OrderForm()
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51HieJBFDbEFsB8WkeMbtU3A1VOoXZiLUDK1R8dZNKmAIaLzLurFz2UR46wQe8NSSJlil7RlmTWpZZNCf8jKqb8wN00bhnWedj1",
        "client_secret": "test client secret",
    }
    return render(request, "checkout/checkout.html", context)
