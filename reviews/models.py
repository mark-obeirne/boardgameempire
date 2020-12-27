from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL)
    review_title = models.CharField(max_length=100)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="reviews")
    date_published = models.DateTimeField(auto_now_add=True)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"{self.review_title} by {self.user_profile}"
