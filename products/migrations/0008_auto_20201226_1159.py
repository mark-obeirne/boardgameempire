# Generated by Django 3.1.3 on 2020-12-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201220_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]