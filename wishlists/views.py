from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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


def add_to_wishlist(request, product_id):
    print("adding product")
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    print(user)
    redirect_url = request.POST.get("redirect_url")
    wishlist = get_object_or_404(Wishlist, user_profile=user)
    print(wishlist.products.all())
    if product in wishlist.products.all():
        print("Already exists!")
        messages.info(request, f"{ product.name } is already on your wishlist")
        return redirect(redirect_url)
    else:
        wishlist.products.add(product)
        print("Product added to wishlist")
        messages.success(request, f"{ product.name } added to your wishlist")
        return redirect(redirect_url)
