from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product, Category, Mechanic
from profiles.models import UserProfile
from wishlists.models import Wishlist
from reviews.models import Review
from django.db.models import Q, Case, When, Value
from django.db.models.functions import Lower, Coalesce
from django.db import models


def all_products(request):
    """ View to display all products currently stocked """
    products = Product.objects.all()
    #products_on_sale = Product.objects.filter(on_sale=True).annotate(current_price="sale_price")
    #products_full_price = Product.objects.filter(on_sale=False).annotate(current_price="price")
    #products = products.annotate(current_price=Case(
    #            When(on_sale=True, then=Value("sale_price"), output_field=models.IntegerField()),
    #            When(on_sale=False, then=Value("price"), output_field=models.IntegerField())))
    
    sort = None
    direction = None
    query = None
    category = None
    mechanic = None
    categories = Category.objects.all()
    mechanics = Mechanic.objects.all()

    if "sort" in request.GET:
        sortkey = request.GET["sort"]
        sort = sortkey
        print(sortkey)
        if sortkey == "name":
            sortkey = "lower_name"
            products = products.annotate(lower_name=Lower("name"))

        if sortkey == "price":
            print("Yes, it's price")
            sortkey = Coalesce("sale_price", "price")
            print("Coalescing")

        if "direction" in request.GET:
            direction = request.GET["direction"]
            if direction == "desc":
                if sortkey == Coalesce("sale_price", "price"):
                    pass
                else:
                    sortkey = f"-{sortkey}"

        if sortkey == Coalesce("sale_price", "price") and direction == "desc":
            print("Trying to reverse Coalescing")
            products = products.order_by(Coalesce("sale_price", "price"))
            products = products.reverse()
            print(products)
        else:
            products = products.order_by(sortkey)

    if "q" in request.GET:
        query = request.GET["q"]
        if not query:
            return redirect(reverse('products'))
        queries = Q(name__icontains=query) | Q(designer__icontains=query) | Q(publisher__icontains=query) 
        products = products.filter(queries)

    if "category" in request.GET:
        category = request.GET["category"]
        category = categories.filter(name=category)
        for entry in category:
            products = products.filter(category=entry.pk)

    if "mechanic" in request.GET:
        mechanic = request.GET["mechanic"]
        mechanic = mechanics.filter(name=mechanic)
        for entry in mechanic:
            products = products.filter(mechanic=entry.pk)

    current_sorting = f"{sort}-{direction}"
    number_of_results = len(products)

    context = {
        "products": products,
        "current_sorting": current_sorting,
        "query": query,
        "current_category": category,
        "current_mechanic": mechanic,
        "number_of_results": number_of_results,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ Return details of an individual product """
    product = get_object_or_404(Product, pk=product_id)
    on_wishlist = False
    review_list = Review.objects.filter(product=product)
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        users_wishlist = Product.objects.filter(wishlist__user_profile=user)
        if product in users_wishlist:
            on_wishlist = True

    context = {
        "product": product,
        "on_wishlist": on_wishlist,
        "review_list": review_list,
    }
    return render(request, "products/product_detail.html", context)


def get_random_game(request):
    """ Return details of a random product """
    product = Product.objects.order_by("?")[0]
    on_wishlist = False
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        users_wishlist = Product.objects.filter(wishlist__user_profile=user)
        if product in users_wishlist:
            on_wishlist = True

    context = {
        "product": product,
        "on_wishlist": on_wishlist,
    }
    return render(request, "products/random.html", context)


def get_deals(request):
    """ Return products currently on sale """
    products = Product.objects.filter(on_sale=True).order_by("sale_price")
    sort = "sale_price"
    direction = "asc"

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

    context = {
        "products": products,
        "current_sorting": current_sorting,
    }

    return render(request, "products/deals.html", context)


def game_of_the_month(request):
    product = Product.objects.filter(game_of_the_month=True)[0]
    print(product)
    on_wishlist = False
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        users_wishlist = Product.objects.filter(wishlist__user_profile=user)
        if product in users_wishlist:
            on_wishlist = True

    context = {
        "product": product,
        "on_wishlist": on_wishlist,
    }
    return render(request, "products/gotm.html", context)
