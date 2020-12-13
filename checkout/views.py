from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
from .forms import OrderForm
from profiles.forms import UserProfileForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from cart.contexts import cart_contents
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        print("Trying to modify")
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        gift_purchase = request.POST.get("gift_purchase", "")
        points_used = int(request.POST.get("points_used"))
        print(points_used)
        amount = 0

        if points_used > 0:
            intent = stripe.PaymentIntent.retrieve(pid)
            print(intent)
            amount = intent.get("amount")
            print(amount)
            points_used = int(points_used / 5)
            print(points_used)
            amount -= points_used
            print(amount)

        stripe.PaymentIntent.modify(pid,
                                    amount=amount,
                                    metadata={
                                        "cart": json.dumps(request.session.get("cart", {})),
                                        "gift_purchase": gift_purchase,
                                        "username": request.user,
                                        "points_used": points_used,
                                    })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry, we can't process your payment at the moment. Please try again later.")
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        print(request.POST)
        cart = request.session.get("cart", {})
        gift_purchase = request.POST.get("gift_purchase", False)
        if gift_purchase == "on":
            gift_purchase = True
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "town_or_city": request.POST["town_or_city"],
            "county_or_state": request.POST["county_or_state"],
            "postcode": request.POST["postcode"],
            "country": request.POST["country"],
            "billing_full_name": request.POST["billing_full_name"],
            "billing_street_address1": request.POST["billing_street_address1"],
            "billing_street_address2": request.POST["billing_street_address2"],
            "billing_town_or_city": request.POST["billing_town_or_city"],
            "billing_county_or_state": request.POST["billing_county_or_state"],
            "billing_country": request.POST["billing_country"],
            "gift_purchase": gift_purchase,
            "points_used": request.POST["points_used"],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

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

            points_used = int(request.POST.get('points_used', 0))
            print("Order Valid")
            print(points_used)
            if points_used > 0:
                current_cart = cart_contents(request)
                cart_total = current_cart["grand_total"]
                points_value = points_used / 5
                cart_total = round(cart_total * 100)
                total_minus_points = cart_total - points_value
                order.grand_total = total_minus_points / 100
                order.save()
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            print("Form is invalid")
            messages.error(request, "Please double check your form details!")
            return redirect(reverse('checkout'))

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

        # Attempt to prefill order form with user info
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    "full_name": profile.default_full_name,
                    "email": profile.default_email,
                    "street_address1": profile.default_street_address1,
                    "street_address2": profile.default_street_address2,
                    "town_or_city": profile.default_town_or_city,
                    "county_or_state": profile.default_county_or_state,
                    "postcode": profile.default_postcode,
                    "country": profile.default_country,
                    "billing_full_name": profile.default_full_name,
                    "billing_street_address1": profile.default_street_address1,
                    "billing_street_address2": profile.default_street_address2,
                    "billing_town_or_city": profile.default_town_or_city,
                    "billing_county_or_state": profile.default_county_or_state,
                    "billing_country": profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            "Did you forget to set your Stripe public key in your environment?")

    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51HieJBFDbEFsB8WkeMbtU3A1VOoXZiLUDK1R8dZNKmAIaLzLurFz2UR46wQe8NSSJlil7RlmTWpZZNCf8jKqb8wN00bhnWedj1",
        "client_secret": intent.client_secret,
        "profile": profile,
    }
    return render(request, "checkout/checkout.html", context)


def checkout_success(request, order_number):
    """ Handle successful submission of form and checkout """
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        profile.loyalty_points += order.points_earned
        profile.loyalty_points -= order.points_used
        profile.save()
        order.user_profile = profile
        order.save()

    messages.success(request, f"Thank you for your order. Your order number is {order_number}. A confirmation email will be sent to {order.email}.")

    if "cart" in request.session:
        del request.session["cart"]

    context = {
        "order": order,
    }
    return render(request, "checkout/checkout_success.html", context)
