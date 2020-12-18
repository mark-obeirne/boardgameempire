from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):

    readonly_fields = ("date_published",)

    fields = ("product", "user_profile", "review_title", "date_published",
              "review_text", "rating",)

    list_display = ("review_title", "product", "user_profile",
                    "date_published", "rating",)

    ordering = ("-date_published",)


admin.site.register(Review, ReviewAdmin)
