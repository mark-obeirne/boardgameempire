from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """ 
    A user profile for saving default delivery details, wishlist, and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=False, blank=False)
    first_name = models.CharField(max_length=80, null=True, blank=True)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county_or_state = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    country = CountryField(blank_label="Country", max_length=40, null=True, blank=True)
    loyalty_points = models.IntegerField(default=0)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update the user profile when user object is saved """
    if created:
        UserProfile.objects.create(user=instance)
    # Alternatively, save profile if user exists
    instance.userprofile.save() 