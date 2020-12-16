from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Mechanic(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    min_age = models.IntegerField()
    playing_time = models.IntegerField()
    year_published = models.IntegerField()
    category = models.ManyToManyField('Category', blank=True, through='CategoryToProduct')
    designer = models.CharField(max_length=254)
    publisher = models.CharField(max_length=254)
    mechanic = models.ManyToManyField('Mechanic', blank=True, through='MechanicOfProduct')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    quantity_sold = models.IntegerField(default=0)
    on_sale = models.BooleanField(default=False, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    game_of_the_month = models.BooleanField(default=False, null=True, blank=True)
    number_reviews = models.IntegerField()
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    boxart = models.ImageField(null=True, blank=True)
    product_image = models.ImageField(null=True, blank=True)
    youtube_video_1 = models.URLField(max_length=1024, null=True, blank=True)
    youtube_video_2 = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class CategoryToProduct(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.product.name} has the following categories: {self.category.name}"


class MechanicOfProduct(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    mechanic = models.ForeignKey(Mechanic, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.product.name} has the following mechanics: {self.mechanic.name}"
