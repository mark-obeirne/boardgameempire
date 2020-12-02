from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models.functions import Lower


def all_products(request):
    """ View to display all products currently stocked """
    products = Product.objects.all()
    sort = None
    direction = None

    if "sort" in request.GET:
        sortkey = request.GET["sort"]
        sort = sortkey
        if "sortkey" == "name":
            sortkey = "lower_name"
            products = products.annotate(lower_name=Lower("name"))

        if "direction" in request.GET:
            direction = request.GET["direction"]
            if direction == "desc":
                sortkey = f"-{sortkey}"
        products = products.order_by(sortkey)

    current_sorting = f"{sort}-{direction}"
    print(current_sorting)
    context = {
        "products": products,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ Return details of an individual product """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)


def get_random_game(request):
    """ Return details of a random product """
    product = Product.objects.order_by("?")[0]
    context = {
        "product": product,
    }
    return render(request, "products/random.html", context)
