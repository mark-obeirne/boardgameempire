from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
from profiles.models import UserProfile
from products.models import Product


def write_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form_data = {
            "review_title": request.POST["review_title"],
            "review_text": request.POST["review_text"],
            "rating": int(request.POST["rating"])
        }
        print(form_data)

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
            messages.error(request, "Sorry, we couldn't submit your review. Please ensure the form is filled out correctly.")

    context = {
        "product": product,
        "form": form,
    }

    return render(request, "reviews/review.html", context)
