from django.shortcuts import render
from django.views.generic.list import ListView

from shop.models import Product


# def index(request):
#     return render(request, 'vitrin/templates/vitrin/index.html')

class IndexView(ListView):
    model = Product
    template_name = 'vitrin/templates/vitrin/index.html'
    context_object_name = 'products'
    paginate_by: 6
