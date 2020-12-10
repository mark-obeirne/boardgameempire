from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from math import ceil


def cart_contents(request):
    items_in_cart = []
    total = 0
    product_count = 0
    cart = request.session.get("cart", {})
    points_earned = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity * product.price
        points_earned += ceil(total * 10)
        product_count += quantity
        items_in_cart.append({
            "product_id": product_id,
            "quantity": quantity,
            "product": product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_FEE
        free_delivery_remainder = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_remainder = 0

    grand_total = total + delivery

    context = {
        "items_in_cart": items_in_cart,
        "total": total,
        "product_count": product_count,
        "points_earned": points_earned,
        "delivery": delivery,
        "free_delivery_remainder": free_delivery_remainder,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
