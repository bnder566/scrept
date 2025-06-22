from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة التحكم الإدارية
    path('admin/', admin.site.urls),

    # تطبيق الحسابات (تسجيل الدخول/التسجيل)
    path('accounts/', include('accounts.urls')),

    # تطبيق الإعلانات (عرض/إضافة سلع)
    path('listings/', include('listings.urls')),

    # تطبيق الصفحات العامة (الرئيسية، تواصل، من نحن)
    path('', include('core.urls')),
]

# دعم عرض ملفات الوسائط عند استخدام DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
