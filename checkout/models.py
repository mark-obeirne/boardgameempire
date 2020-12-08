from django.db import models
import uuid
from django.db.models import Sum
from django.db.models.functions import Round
from django.conf import settings
from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county_or_state = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    points_earned = models.IntegerField(null=False, blank=False, editable=False, default=0)
    points_used = models.IntegerField(null=False, blank=False, editable=False, default=0)
    delivery_cost = models.DecimalField(max_digits=4, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    billing_full_name = models.CharField(max_length=60, null=False, blank=False)
    billing_street_address1 = models.CharField(max_length=80, null=False, blank=False)
    billing_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    billing_town_or_city = models.CharField(max_length=40, null=False, blank=False)
    billing_county_or_state = models.CharField(max_length=40, null=True, blank=True)
    billing_country = models.CharField(max_length=40, null=False, blank=False)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def __str__(self):
        return self.order_number

    def generate_order_number(self):
        """ Generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Override the original save method to set the order number if not already set """
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

    def update_grand_total(self):
        """ Update grand total each time a line item is added, taking delivery costs into account """
        self.order_total = self.lineitems.aggregate(Sum("lineitem_total"))["lineitem_total__sum"] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_FEE
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def update_points_earned(self):
        """ Update points earned on an order each time a line item is added """
        self.points_earned = self.lineitems.aggregate(Sum("lineitem_points_earned"))["lineitem_points_earned__sum"]


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name="lineitems")
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    lineitem_points_earned = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return f"SKU {self.product.sku} on order {self.order.order_number}"

    def save(self, *args, **kwargs):
        """ Override original save method to set the lineitem total and the loyalty points earned """
        self.lineitem_total = self.product.price * self.quantity
        self.lineitem_points_earned = Round(self.lineitem_total * 10)
        super().save(*args, **kwargs)
