from django.shortcuts import render
from django.http import JsonResponse


def add_to_cart(request):
    data = dict(request.POST)
    # print(data)


    return JsonResponse(data=data, safe=False)
