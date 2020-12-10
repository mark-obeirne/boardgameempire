from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib import messages


def profile(request):
    """ Display the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Failed to update profile. Please ensure form is valid")
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    context = {
        "profile": profile,
        "form": form,
        "orders": orders,
    }

    return render(request, "profiles/profile.html", context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, "checkout/checkout_success.html", context)
