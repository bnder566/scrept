from django.urls import path
from .views import user_products, add_product

app_name = 'userproducts'

urlpatterns = [
    path('', user_products, name='user_products'),
    path('add/', add_product, name='add_product'),
]
