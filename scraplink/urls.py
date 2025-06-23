# scraplink/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_view  # لتسجيل الدخول مباشرة من /login/

urlpatterns = [
    # لوحة تحكم المشرف
    path('admin/', admin.site.urls),

    # تسجيل الدخول مباشرة عبر /login/
    path('login/', login_view, name='direct_login'),  # لتفادي تعارض الاسم مع accounts:login

    # روابط الحسابات (تسجيل جديد - تسجيل الدخول - تسجيل الخروج)
    path('accounts/', include('accounts.urls')),

    # روابط الإعلانات (عرض وإضافة الإعلانات)
    path('listings/', include('listings.urls')),

    # روابط الصفحات العامة مثل الرئيسية ومن نحن وتواصل معنا
    path('', include('core.urls')),
]

# دعم ملفات الوسائط أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
