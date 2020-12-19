from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name="about_us"),
    path('loyalty/', views.loyalty, name="loyalty"),
    path('returns/', views.returns, name="returns"),
    path('contact/', views.contact_us, name="contact_us"),
    path('contact-success/', views.contact_success, name="contact_success"),
]
