from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from profiles.models import UserProfile
from products.models import Product
from .models import Wishlist
from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    """
    Get and display user's wishlist if they have one created or create one if
    they have not
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist, created = Wishlist.objects.get_or_create(user_profile=profile)
    wishlisted_products = Product.objects.filter(
        wishlist__user_profile=profile)

    context = {
        "profile": profile,
        "wishlisted_products": wishlisted_products,
    }

    return render(request, "wishlists/wishlist.html", context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Add selected product to user's wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    redirect_url = request.POST.get("redirect_url")
    wishlist, created = Wishlist.objects.get_or_create(user_profile=user)

    if product in wishlist.products.all():
        messages.info(request, f"{ product.name } is already on your wishlist")
        return redirect(redirect_url)
    else:
        wishlist.products.add(product)
        messages.success(request, f"{ product.name } added to your wishlist")
        return redirect(redirect_url)


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove selected product from user's wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    redirect_url = request.POST.get("redirect_url")
    wishlist = get_object_or_404(Wishlist, user_profile=user)
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request,
                         f"{ product.name } removed from your wishlist")
        return redirect(redirect_url)
    else:
        messages.error(request, f"{ product.name } was not on your wishlist")
        return redirect(redirect_url)


@login_required
def delete_wishlist(request):
    """
    Delete entire wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    redirect_url = request.POST.get("redirect_url")
    wishlist = get_object_or_404(Wishlist, user_profile=user)
    wishlist.products.clear()
    return redirect(redirect_url)
