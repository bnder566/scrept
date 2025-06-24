from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_view  # تسجيل الدخول مباشرة من /login/

urlpatterns = [
    # لوحة تحكم المشرف
    path('admin/', admin.site.urls),

    # تسجيل الدخول مباشرة عبر /login/
    path('login/', login_view, name='direct_login'),

    # روابط الحسابات: تسجيل جديد، تسجيل دخول، تسجيل خروج
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # روابط الإعلانات (عرض، إضافة، تعديل، حذف المنتجات)
    path('listings/', include('listings.urls')),

    # روابط الصفحات العامة مثل: الرئيسية، من نحن، تواصل معنا
    path('', include('core.urls')),

    # ✅ روابط لوحة تحكم المستخدم personal products
    path('my-products/', include('userproducts.urls', namespace='userproducts')),
]

# دعم ملفات الوسائط أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
