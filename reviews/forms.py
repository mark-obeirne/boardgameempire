from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ("product", "user_profile", "date_published")

        def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated labels
            and set autofocus
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                "review_title": "Title Your Review",
                "review_text": "Write Your Review",
                "rating": "Rating",
            }

            self.fields["review_title"].widget.attrs["autofocus"] = True
            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
                self.fields[field].label = False
