from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile
from products.models import Product
from .models import Wishlist


def wishlist(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = Product.objects.filter(wishlist__user_profile=profile)
    print(profile)
    print(wishlist)

    context = {
        "profile": profile,
        "wishlist": wishlist,
    }

    return render(request, "wishlists/wishlist.html", context)
