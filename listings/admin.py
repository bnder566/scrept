from django.contrib import admin
from .models import Product  # ✅ استخدم Product بدل Listing

admin.site.register(Product)
