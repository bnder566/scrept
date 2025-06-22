from django.urls import path
from .views import listing_list, create_listing

urlpatterns = [
    path('', listing_list, name='listing_list'),
    path('create/', create_listing, name='create_listing'),
]
