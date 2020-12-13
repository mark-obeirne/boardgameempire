from django.shortcuts import get_object_or_404
from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist


def wishlist_contents(request):
    """ Make user's wishlist available across apps """
    wishlisted_items = None
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        wishlist, created = Wishlist.objects.get_or_create(user_profile=profile)
        wishlisted_products = Product.objects.filter(wishlist__user_profile=profile)
        print(wishlisted_products)

    context = {
        "wishlisted_products": wishlisted_products,
    }
    print(context)
    return context
