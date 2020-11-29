from django.shortcuts import render
from .models import Product
from django.db.models.functions import Lower


def all_products(request):
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
