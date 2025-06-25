from django.urls import path
from .views import home_view, about_view, contact_view, services_view

# اسم التطبيق لتسهيل الاستدعاء في reverse() أو {% url %}
app_name = 'core'

urlpatterns = [
    # الصفحة الرئيسية
    path('', home_view, name='home'),

    # صفحة من نحن
    path('about/', about_view, name='about'),

    # صفحة تواصل معنا
    path('contact/', contact_view, name='contact'),

    # صفحة الخدمات
    path('services/', services_view, name='services'),
]
