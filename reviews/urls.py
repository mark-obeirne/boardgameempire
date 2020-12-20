from django.urls import path
from . import views

urlpatterns = [
    path("review/<product_id>", views.write_review, name="write_review"),
    path("all-reviews/<product_id>", views.all_reviews, name="all_reviews"),
    path("full-review/<review_id>", views.full_review, name="full_review"),
]
