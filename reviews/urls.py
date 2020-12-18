from django.urls import path
from . import views

urlpatterns = [
    path("review/<product_id>", views.write_review, name="write_review"),
]
