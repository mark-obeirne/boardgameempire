from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product, Category, Mechanic
from profiles.models import UserProfile
from reviews.models import Review
from django.db.models import Q
from django.db.models.functions import Lower, Coalesce
from django.contrib import messages


def all_products(request):
    """
    Display all products currently stocked and take any user selected sort and
    direction into account when sorting
    """

    products = Product.objects.all()

    # Set variables to None to handle basic behaviour without user input
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
        if sortkey == "name":
            sortkey = "lower_name"
            products = products.annotate(lower_name=Lower("name"))

        if sortkey == "price":
            """
            Return first non-null value so that sale and regular priced
            products can be sorted together
            """
            sortkey = Coalesce("sale_price", "price")

        if "direction" in request.GET:
            direction = request.GET["direction"]
            if direction == "desc":
                if sortkey == Coalesce("sale_price", "price"):
                    # Must be handled separately to avoid error
                    pass
                else:
                    sortkey = f"-{sortkey}"

        if sortkey == Coalesce("sale_price", "price") and direction == "desc":
            # Reverse ordering of Coalesce if direction is descending
            products = products.order_by(Coalesce("sale_price", "price"))
            products = products.reverse()
        else:
            products = products.order_by(sortkey)

    if "q" in request.GET:
        query = request.GET["q"]
        if not query:
            messages.error(request, "You did not enter a search term")
            return redirect(reverse('products'))
        queries = Q(
            name__icontains=query) | Q(
                designer__icontains=query) | Q(
                    publisher__icontains=query)
        products = products.filter(queries)

    if "category" in request.GET:
        category = request.GET["category"]
        query = category
        category = categories.filter(name=category)
        for entry in category:
            products = products.filter(category=entry.pk)

    if "mechanic" in request.GET:
        mechanic = request.GET["mechanic"]
        query = mechanic
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
    """
    Return details of an individual product and determine if product is on
    user's wishlist (if user is logged in)
    """
    product = get_object_or_404(Product, pk=product_id)
    average_rating = 0
    on_wishlist = False
    latest_reviews = Review.objects.filter(
        product=product).order_by("-date_published")[0:2]

    if product.number_reviews > 0:
        average_rating = product.total_rating / product.number_reviews

    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        users_wishlist = Product.objects.filter(wishlist__user_profile=user)
        if product in users_wishlist:
            on_wishlist = True

    context = {
        "product": product,
        "on_wishlist": on_wishlist,
        "latest_reviews": latest_reviews,
        "average_rating": average_rating,
    }
    return render(request, "products/product_detail.html", context)


def get_random_game(request):
    """
    Return details of a random product and determine if product is on user's
    wishlist (if user is logged in)
    """

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
    """
    Find product marked game of the month and determine if it's on the user's
    wishlist (if user is logged in)
    """
    product = Product.objects.filter(game_of_the_month=True)[0]
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
