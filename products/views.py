from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product
from django.db.models import Q
from django.db.models.functions import Lower


def all_products(request):
    """ View to display all products currently stocked """
    products = Product.objects.all()
    sort = None
    direction = None
    query = None

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

    if "q" in request.GET:
        query = request.GET["q"]
        if not query:
            return redirect(reverse('products'))
        queries = Q(name__icontains=query) | Q(designer__icontains=query) | Q(publisher__icontains=query) 
        products = products.filter(queries)

    current_sorting = f"{sort}-{direction}"

    context = {
        "products": products,
        "current_sorting": current_sorting,
        "query": query,
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


def get_deals(request):
    """ Return products currently on sale """
    products = Product.objects.filter(on_sale=True)
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

    context = {
        "products": products,
    }
    return render(request, "products/deals.html", context)


def game_of_the_month(request):
    product = Product.objects.filter(game_of_the_month=True)[0]
    print(product)
    context = {
        "product": product,
    }
    return render(request, "products/gotm.html", context)
