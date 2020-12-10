from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total", "lineitem_points_earned",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ("order_number", "order_date", "delivery_cost",
                       "order_total", "grand_total", "points_earned",)

    fields = ("order_number", "user_profile", "order_date", "full_name",
              "email", "street_address1", "town_or_city",
              "county_or_state", "postcode", "country",
              "order_total", "delivery_cost", "grand_total",
              "points_earned", "points_used", "gift_purchase",
              "billing_full_name", "billing_street_address1",
              "billing_street_address2", "billing_town_or_city",
              "billing_county_or_state", "billing_country",)

    list_display = ("order_number", "order_date", "full_name", "order_total", "delivery_cost", "grand_total", "points_earned", "points_used",)

    ordering = ("-order_date",)


admin.site.register(Order, OrderAdmin)
