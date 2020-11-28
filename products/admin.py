from django.db import models
from django.contrib import admin
from .models import Category, Mechanic, Product, CategoryToProduct, MechanicOfProduct

# Register your models here.


class CategoryToProductAdminInline(admin.TabularInline):
    model = CategoryToProduct
    extra = 1


class MechanicOfProductAdminInline(admin.TabularInline):
    model = MechanicOfProduct
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "price",
        "inventory",
        "on_sale",
        "game_of_the_month"
    )

    ordering = ("name",)

    inlines = [CategoryToProductAdminInline, MechanicOfProductAdminInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

    ordering = ("friendly_name",)


class MechanicAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

    ordering = ("friendly_name",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Mechanic, MechanicAdmin)
