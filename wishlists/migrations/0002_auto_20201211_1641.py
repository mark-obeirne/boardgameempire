# Generated by Django 3.1.3 on 2020-12-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_quantity_sold'),
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
        migrations.DeleteModel(
            name='ProductToWishlist',
        ),
    ]
