from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from wishlists.models import Wishlist
from products.models import Product
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """
    Display the user's profile if they have saved details previously and handle
    updates to details via POST request
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist, created = Wishlist.objects.get_or_create(user_profile=profile)
    wishlisted_products = Product.objects.filter(
        wishlist__user_profile=profile)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request,
                "Failed to update profile. Please ensure form is valid")
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all().order_by("-order_date")

    context = {
        "profile": profile,
        "form": form,
        "orders": orders,
        "wishlisted_products": wishlisted_products,
    }

    return render(request, "profiles/profile.html", context)


def order_history(request, order_number):
    """
    Display details of an individual order and indicate that user is accessing
    page from their profile
    """
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, "checkout/checkout_success.html", context)
