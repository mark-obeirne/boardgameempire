from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
from profiles.models import UserProfile
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def write_review(request, product_id):
    """
    Render form for user to submit review of a selected product and handle
    submission of review
    """
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()
    user_profile = UserProfile.objects.get(user=request.user)
    all_reviews = list(Review.objects.filter(
        product=product))
    for review in all_reviews:
        if user_profile == review.user_profile:
            messages.error(request,
                           f"You have already reviewed {product.name}")
            return redirect('product_detail', product.id)

    if request.method == "POST":
        form_data = {
            "review_title": request.POST["review_title"],
            "review_text": request.POST["review_text"],
            "rating": int(request.POST["rating"])
        }

        form = ReviewForm(request.POST)
        if form.is_valid():
            review_title = request.POST["review_title"]
            review_text = request.POST["review_text"]
            rating = int(request.POST["rating"])

            review = Review()
            review.product = product
            review.review_title = review_title
            review.review_text = review_text
            review.user_profile = user_profile
            review.rating = rating
            review.save()

            product.total_rating += review.rating
            product.number_reviews += 1
            product.save()
            messages.success(request, "Thank you for your review")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           "Sorry, we couldn't submit your review."
                           "Please ensure the form is filled out correctly.")

    context = {
        "product": product,
        "form": form,
    }

    return render(request, "reviews/review.html", context)


def all_reviews(request, product_id):
    """
    Display all reviews for a selected product
    """
    product = get_object_or_404(Product, pk=product_id)
    all_reviews = Review.objects.filter(
        product=product).order_by("-date_published")

    context = {
        "product": product,
        "all_reviews": all_reviews,
    }

    return render(request, "reviews/all-reviews.html", context)


def full_review(request, review_id):
    """
    Show individual review in full for a selected product
    """
    full_review = get_object_or_404(Review, pk=review_id)

    context = {
        "full_review": full_review,
    }

    return render(request, "reviews/full-review.html", context)
