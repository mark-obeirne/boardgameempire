from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product
from django.contrib import messages
from django.utils.safestring import mark_safe


def view_cart(request):
    """ View items currently in cart """
    cart = request.session.get("cart", {})
    print(cart)
    return render(request, "cart/cart.html")


def add_to_cart(request, product_id):
    """ Add a product to the cart """
    product = Product.objects.get(pk=product_id)
    cart = request.session.get("cart", {})
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.success(request, f"{product.name} added to cart. You have {cart[product_id]}x {product.name} in your cart")
    else:
        cart[product_id] = quantity
        messages.success(request, f"{product.name} added to cart. You have {cart[product_id]}x {product.name} in your cart")

    request.session["cart"] = cart
    return redirect(redirect_url)


def update_cart(request, product_id):
    """ Update the quantity of a product in the user's cart """
    cart = request.session.get("cart", {})
    new_quantity = int(request.POST.get("quantity"))
    cart[product_id] = new_quantity
    request.session["cart"] = cart
    return redirect(reverse("view_cart"))


def remove_from_cart(request, product_id):
    """ Remove specified product from user's cart """
    cart = request.session.get("cart", {})
    try:
        cart.pop(product_id)

        request.session["cart"] = cart
        messages.add_message(request, messages.INFO, 'Item removed.')
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
