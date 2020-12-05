from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('random/', views.get_random_game, name="get_random_game"),
    path('deals/', views.get_deals, name="get_deals"),
]
