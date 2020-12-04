from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product


def view_cart(request):
    """ View items currently in cart """
    cart = request.session.get("cart", {})
    print(cart)
    return render(request, "cart/cart.html")


def add_to_cart(request, product_id):
    """ Add a product to the cart """
    cart = request.session.get("cart", {})
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session["cart"] = cart
    return redirect(redirect_url)


def update_cart(request, product_id):
    """ Update the quantity of a product in the user's cart """
    cart = request.session.get("cart", {})
    new_quantity = int(request.POST.get("quantity"))
    cart[product_id] = new_quantity
    request.session["cart"] = cart
    return redirect(reverse("view_cart"))
