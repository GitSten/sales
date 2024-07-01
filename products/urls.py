from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='index'),
    path('new-products/', views.new_products, name='new_products'),
    path('product-changes/', views.product_changes, name='product_changes'),
    path('discontinued-products/', views.discontinued_products, name='discontinued_products'),
    path('info/', views.info, name='info'),
]
