from django.urls import path
from .views import (
    listing_list,
    create_listing,
    pending_listings,
    approve_listing,
    reject_listing
)

app_name = 'listings'

urlpatterns = [
    # 👥 للمستخدم العادي
    path('', listing_list, name='listing_list'),
    path('create/', create_listing, name='create_listing'),

    # 🛠️ للمشرف
    path('admin/pending/', pending_listings, name='pending_listings'),
    path('admin/approve/<int:pk>/', approve_listing, name='approve_listing'),
    path('admin/reject/<int:pk>/', reject_listing, name='reject_listing'),
]
