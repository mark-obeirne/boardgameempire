from django.shortcuts import render, redirect


def view_cart(request):
    """ View items currently in cart """
    return render(request, "cart/cart.html")


def add_to_cart(request, product_id):
    """ Add a product to the cart """
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})
    redirect_url = request.POST.get("redirect_url")

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session["cart"] = cart
    print(cart)
    return redirect(redirect_url)
