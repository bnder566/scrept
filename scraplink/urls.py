from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# استيراد العروض المباشرة
from accounts.views import login_view
from listings.views import add_product
from core.views import sales_view

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # روابط مباشرة
    path('login/', login_view, name='direct_login'),
    path('add-product/', add_product, name='direct_add_product'),
    path('sales/', sales_view, name='sales'),

    # تطبيقات المشروع
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('listings/', include('listings.urls')),
    path('', include('core.urls')),
    path('my-products/', include('userproducts.urls', namespace='userproducts')),

    # ✅ تفعيل تطبيق الطلبات (تأكد أن اسم المجلد هو orders وليس orderapp)
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
]

# إعدادات media عند تفعيل وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
