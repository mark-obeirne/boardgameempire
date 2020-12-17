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

    # If user has stayed on a page for a while before adding products to cart, prevent them from adding more copies of a product to their cart than there are in stock
    if quantity > product.inventory:
        messages.error(request, f"Sorry! We don't have enough copies of {product.name} in stock to complete your request right now")
        return redirect(redirect_url)

    if product_id in list(cart.keys()):
        current_quantity = cart[product_id]
        # Prevent user from adding quantities of a product to cart that would exceed the inventory in stock  
        if current_quantity + quantity > product.inventory:
            messages.error(request,
                f"Sorry! You are trying to add too many copies of {product.name} to your cart. You currently have {cart[product_id]}x {product.name} in your cart")
            return redirect(redirect_url)
        else:
            cart[product_id] += quantity
            messages.success(request, f"{product.name} added to cart. You have {cart[product_id]}x {product.name} in your cart")
    else:
        cart[product_id] = quantity
        messages.success(request, f"{product.name} added to cart. You have {cart[product_id]}x {product.name} in your cart")

    request.session["cart"] = cart
    return redirect(redirect_url)


def update_cart(request, product_id):
    """ Update the quantity of a product in the user's cart """
    product = Product.objects.get(pk=product_id)
    cart = request.session.get("cart", {})
    new_quantity = int(request.POST.get("quantity"))
    cart[product_id] = new_quantity
    messages.success(request, f"Cart updated. You now have {cart[product_id]}x {product.name} in your cart")
    request.session["cart"] = cart
    return redirect(reverse("view_cart"))


def remove_from_cart(request, product_id):
    """ Remove specified product from user's cart """
    product = Product.objects.get(pk=product_id)
    cart = request.session.get("cart", {})
    try:
        cart.pop(product_id)

        request.session["cart"] = cart
        messages.success(request, f"{product.name} removed from your cart")
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
