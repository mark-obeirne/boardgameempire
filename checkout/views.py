from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from cart.contexts import cart_contents
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get("cart", {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "town_or_city": request.POST["town_or_city"],
            "county_or_state": request.POST["county_or_state"],
            "postcode": request.POST["postcode"],
            "country": request.POST["country"],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for product_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=product_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, ("One of the products in your bag couldn't be found in our database. We're very sorry; please contact us for assistance!"))
                    order.delete()
                    return redirect(reverse("view_cart"))
            return redirect(reverse('checkout_success', args=[order.order_number]))

    else:
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
        "client_secret": intent.client_secret,
    }
    return render(request, "checkout/checkout.html", context)


def checkout_success(request, order_number):
    """ Handle successful submission of form and checkout """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f"Thank you for your order. Your order number is {order_number}. A confirmation email will be sent to {order.email}.")

    if "cart" in request.session:
        del request.session["cart"]

    context = {
        "order": order,
    }
    return render(request, "checkout/checkout_success.html", context)
