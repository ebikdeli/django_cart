# Generated by Django 4.0.5 on 2022-06-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_slug_product_slug_alter_product_image_and_more'),
        ('cart', '0002_alter_cart_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='cart_products', to='shop.product'),
        ),
    ]