from django.urls import path

from . import views


app_name = 'shop'

urlpatterns = [
    # These 3-4 below 'path' show us how we can use same view with same 'name' but with diffrent url to get same thing!
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    # Detail view only use 'pk' or 'slug' field to get current object in 'DetailView.get_object(queryset) method.
    # In this case 'slug' field is as 'name' field so we must not use 'name' field in urlpatterns otherwise django raise error:
    # path('product/<str:name>/', views.ProductDetail.as_view(), name='product_detail'),
    path('product/<str:name>/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('product/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
]
