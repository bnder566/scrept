from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class UserProduct(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="صاحب المنتج")
    title = models.CharField(max_length=100, verbose_name="عنوان المنتج")
    description = models.TextField(verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج المستخدم"
        verbose_name_plural = "منتجات المستخدم"

    def __str__(self):
        return self.title
