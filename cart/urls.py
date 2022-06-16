from django.urls import path

from . import views


app_name = 'cart'

urlpatterns = [
    path('add/prodcut/', views.add_to_cart, name='add_to_cart'),
]

