from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.popular_list, name='popular_list'),
    path('menu/', views.product_list, name='product_list'),
    path('menu/category/<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
]
