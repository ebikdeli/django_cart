from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from .models import Cart
from shop.models import Product


class CartView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
# class CartView(LoginRequiredMixin, ListView):
    template_name = 'cart/templates/cart/cart_view.html'
    model = Cart
    context_object_name = 'cart'
    permission_required = 'cart.can_see_cart'

    def get_queryset(self):
        # print(self.__dict__)
        qs = Cart.objects.filter(user=self.request.user)
        if qs.exists():
            return qs.last()
        return qs.none()


def add_to_cart(request):
    if request.method == 'POST':
        data = dict(request.POST)
        cart = request.user.cart_user
        product_id = int(data['product_id'][0])
        product = Product.objects.get(id=product_id)
        numbers = int(data['numbers'][0])

        # Change cart items and price by new product
        # cart.products.remove(product)
        cart.products.add(product)
        cart.total_items += numbers
        cart.total_price += numbers * product.price
        cart.save()

        # Create CartItem for new product or add number and price to the already created CartItem
        qs = cart.cart_item_cart.filter(product=product)
        if qs.exists():
            print('itemcart already exists')
            ci = qs.last()
            ci.number = numbers
            ci.price = numbers * product.price
            ci.save()
        else:
            print('new itemcart created')
            cart.cart_item_cart.create(product=product, number=numbers, price=numbers * product.price)
        print(cart.cart_item_cart.all())
        return JsonResponse(data=data, safe=False)

    return JsonResponse(data={'status': 'NOK'}, safe=False)
