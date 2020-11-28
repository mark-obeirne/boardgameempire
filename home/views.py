from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to display the index page """
    best_seller = Product.objects.order_by('quantity_sold')[0]
    context = {
        "best_seller": best_seller
    }
    return render(request, "home/index.html", context)
