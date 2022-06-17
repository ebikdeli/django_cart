from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Cart


class CartView(LoginRequiredMixin, ListView):
    template_name = 'cart/templates/cart/cart_view.html'
    model = Cart
    context_object_name = 'cart'

    def get_queryset(self):
        # print(self.__dict__)
        qs = Cart.objects.filter(user=self.request.user)
        if qs.exists():
            return qs.last()
        return qs.none()


def add_to_cart(request):
    data = dict(request.POST)

    return JsonResponse(data=data, safe=False)
