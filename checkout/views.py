from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from cart.contexts import cart_contents
import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Modify Stripe intent based on details collected from form, including points
    used and the effect on the amount to charge if applicable
    """
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        gift_purchase = request.POST.get("gift_purchase", "")
        if request.user.is_authenticated:
            points_used = int(request.POST.get("points_used"), 0)
            intent = stripe.PaymentIntent.retrieve(pid)
            amount = intent.get("amount")

            if points_used > 0:
                points_used = int(points_used / 5)
                amount -= points_used

            stripe.PaymentIntent.modify(pid,
                                        amount=amount,
                                        metadata={
                                            "cart": json.dumps(
                                                request.session.get(
                                                    "cart", {}
                                                    )
                                                    ),
                                            "gift_purchase": gift_purchase,
                                            "username": request.user,
                                            "points_used": points_used,
                                        })
        else:
            stripe.PaymentIntent.modify(pid,
                                        metadata={
                                            "cart": json.dumps(
                                                request.session.get(
                                                    "cart", {}
                                                    )
                                                    ),
                                            "gift_purchase": gift_purchase,
                                            "username": request.user,
                                        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request,
                       "Sorry, we can't process your payment at the moment. "
                       "Please try again later."
                       )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Display form either prefilled if user has entered details in their profile
    or blank. Handle checkout and saving of order upon receipt of POST request
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get("cart", {})
        gift_purchase = request.POST.get("gift_purchase", False)
        if gift_purchase == "on":
            gift_purchase = True
        if request.user.is_authenticated:
            # Include points used in form data if user is logged in
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
                "billing_street_address1": request.POST[
                    "billing_street_address1"],
                "billing_street_address2": request.POST[
                    "billing_street_address2"],
                "billing_town_or_city": request.POST["billing_town_or_city"],
                "billing_county_or_state": request.POST[
                    "billing_county_or_state"],
                "billing_country": request.POST["billing_country"],
                "gift_purchase": gift_purchase,
                "points_used": request.POST["points_used"],
            }

        else:
            # Set points used to 0
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
                "billing_street_address1": request.POST[
                    "billing_street_address1"],
                "billing_street_address2": request.POST[
                    "billing_street_address2"],
                "billing_town_or_city": request.POST["billing_town_or_city"],
                "billing_county_or_state": request.POST[
                    "billing_county_or_state"],
                "billing_country": request.POST["billing_country"],
                "gift_purchase": gift_purchase,
                "points_used": 0,
            }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Save order
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

            for product_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=product_id)
                    # Check if quantity is greater than currently available (in
                    # case other users made purchases)
                    if quantity > product.inventory:
                        messages.error(request,
                                       (f"Sorry! We currently have "
                                        f"{product.inventory}x {product.name} "
                                        "in stock. Please update your cart."))
                        order.delete()
                        return redirect(reverse("view_cart"))
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request,
                                   ("One of the products in your bag couldn't "
                                    "be found in our database. We're very "
                                    "sorry; please contact us for assistance!"
                                    ))
                    order.delete()
                    return redirect(reverse("view_cart"))

            if request.user.is_authenticated:
                # Get points used and update cart total if customer used points
                points_used = int(request.POST.get('points_used', 0))
                if points_used > 0:
                    current_cart = cart_contents(request)
                    cart_total = current_cart["grand_total"]
                    points_value = points_used / 5
                    cart_total = round(cart_total * 100)
                    total_minus_points = cart_total - points_value
                    order.grand_total = total_minus_points / 100
                    order.save()
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "Please double check your form details!")
            return redirect(reverse('checkout'))

    else:
        # GET request
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
            "Did you forget to set your Stripe public key in your environment?"
            )

    if request.user.is_authenticated:
        context = {
            "order_form": order_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
            "profile": profile,
        }
        return render(request, "checkout/checkout.html", context)
    else:
        context = {
            "order_form": order_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
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

    messages.success(request,
                     f"Thank you for your order. Your order number is "
                     f"{order_number}. A confirmation email will be sent to "
                     f"{order.email}.")

    if "cart" in request.session:
        del request.session["cart"]

    context = {
        "order": order,
    }
    return render(request, "checkout/checkout_success.html", context)
