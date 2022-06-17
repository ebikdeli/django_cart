from django.db import models
from django.conf import settings
from django.utils.text import slugify

import uuid


class Cart(models.Model):
    cart_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart_user')
    products = models.ManyToManyField('shop.Product', related_name='cart_products')
    total_items = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.username}_cart'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.cart_id)
        super().save(*args, **kwargs)


class CartItem(models.Model):
    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE, related_name='cart_item_cart')
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='cart_item_product')
    number = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0, decimal_places=0, max_digits=10)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'item: {self.product.name} - cart id: {self.cart.id}'
