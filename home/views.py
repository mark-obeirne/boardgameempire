from django.shortcuts import render
from products.models import Product
from profiles.models import UserProfile


def index(request):
    """ A view to display the index page """
    best_seller = Product.objects.order_by('-quantity_sold')[0]
    on_wishlist = False

    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        users_wishlist = Product.objects.filter(wishlist__user_profile=user)
        if best_seller in users_wishlist:
            on_wishlist = True

    context = {
        "best_seller": best_seller,
        "on_wishlist": on_wishlist,
    }

    return render(request, "home/index.html", context)
