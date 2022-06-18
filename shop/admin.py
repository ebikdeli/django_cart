from atexit import register
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Product, Category


admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    pass
