from django.shortcuts import render, get_object_or_404
# from django.core.paginator import Paginator
from .models import Product, Category


def popular_list(request):
    products = Product.objects.filter(available=True)[:4]
    return render(request,'main/index/index.html', {'products':products})

