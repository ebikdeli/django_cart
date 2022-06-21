from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Product


class ProductDetail(PermissionRequiredMixin, DetailView):
# class ProductDetail(DetailView):
    model = Product
    permission_required = ('shop.can_go_shopping', 'cart.can_see_cart')
    
    # queryset = Product.objects.all()
    template_name = 'shop/templates/shop/product_detail.html'
    context_object_name = 'product'
    # By default 'slug_field' and 'slug_url_kwarg' attributes are equal to 'slug' field!
    # slug_field = 'slug'
    # slug_url_kwarg = 'slug'

    # def get_object(self, queryset=None):
        # print(self.kwargs)
        # return super().get_object(queryset)
