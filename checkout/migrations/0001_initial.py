# Generated by Django 3.1.3 on 2020-12-06 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_product_quantity_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(max_length=80)),
                ('town_or_city', models.CharField(max_length=40)),
                ('county_or_state', models.CharField(blank=True, max_length=40, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(max_length=40)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('points_earned', models.IntegerField(default=0, editable=False)),
                ('points_used', models.IntegerField(default=0, editable=False)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
