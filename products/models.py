from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, blank=True, default=name)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Mechanic(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, blank=True, default=name)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    min_players = models.IntegerField(null=False, blank=False)
    max_players = models.IntegerField(null=False, blank=False)
    min_age = models.IntegerField(null=False, blank=False)
    playing_time = models.IntegerField(null=False, blank=False)
    year_published = models.IntegerField(null=False, blank=False)
    category = models.ManyToManyField('Category',
                                      blank=True,
                                      through='CategoryToProduct')
    designer = models.CharField(max_length=254, null=False, blank=False)
    publisher = models.CharField(max_length=254, null=False, blank=False)
    mechanic = models.ManyToManyField('Mechanic',
                                      blank=True,
                                      through='MechanicOfProduct')
    inventory = models.IntegerField(default=0, null=False, blank=False)
    quantity_sold = models.IntegerField(default=0)
    on_sale = models.BooleanField(default=False, null=True, blank=True)
    sale_price = models.DecimalField(
                                     max_digits=6,
                                     decimal_places=2,
                                     null=True,
                                     blank=True
                                     )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    game_of_the_month = models.BooleanField(
                                            default=False,
                                            null=True,
                                            blank=True)
    number_reviews = models.IntegerField(default=0)
    total_rating = models.IntegerField(default=0)
    boxart = models.ImageField(blank=True, null=True)
    product_image = models.ImageField(blank=True, null=True)
    youtube_video_1 = models.CharField(max_length=50, blank=True, null=True)
    youtube_video_2 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_current_price(self):
        if self.on_sale:
            return self.sale_price
        else:
            return self.price


class CategoryToProduct(models.Model):
    product = models.ForeignKey(
                                Product,
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL
                                )
    category = models.ForeignKey(
                                 Category,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL
                                 )

    def __str__(self):
        return f"Manage {self.category.name}"


class MechanicOfProduct(models.Model):
    product = models.ForeignKey(
                                Product,
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL
                                )
    mechanic = models.ForeignKey(
                                 Mechanic,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL
                                 )

    def __str__(self):
        return f"Manage {self.mechanic.name}"
