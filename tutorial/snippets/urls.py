from django.urls import path
from . import views

urlpatterns = [
    path('customer-api/', views.customer_api, name = 'customer_api'),
    path('latest-products/', views.LatestProductsList, name = 'LatestProductsList'),
    path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetail.as_view()), 
]