from django.shortcuts import render, get_object_or_404
# from django.core.paginator import Paginator
from .models import Product, Category


def popular_list(request):
    pizza_category_popular = Category.objects.filter(name__iexact="пицца").first()  
    products = Product.objects.filter(category=pizza_category_popular)[:4]
    return render(request,'main/index/index.html', {'products':products})

# def product_list(request):
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     return render(request,
#                   'main/product/list.html', {'products':products, 'categories':categories})
# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category,
#                                      slug=category_slug)
#     return render(request,
#                   'main/product/list.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products,
#                    'slug_url': category_slug})
    
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, available=True)
    else:
        products = Product.objects.filter(available=True).order_by('category')

    return render(request, 'main/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })