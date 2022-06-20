from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from sorl.thumbnail import ImageField


class Category(models.Model):
    sub = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_category', blank=True, null=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}'

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey('shop.Category', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    # image = models.ImageField(blank=True, null=True)
    image = ImageField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        if self.brand:
            return f'{self.brand}_{self.name}'
        return f'{self.name}'
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"pk": self.pk, 'name': self.name})
