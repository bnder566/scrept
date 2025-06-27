from django.db import models

class Product(models.Model):
    # خيارات التصنيفات
    CATEGORY_CHOICES = [
        ('electronics', 'إلكترونيات'),
        ('furniture', 'أثاث'),
        ('metal', 'معادن'),
        ('other', 'أخرى'),
    ]

    # خيارات الحالة
    CONDITION_CHOICES = [
        ('new', 'جديد'),
        ('used', 'مستعمل'),
    ]

    name = models.CharField(max_length=255, verbose_name='اسم المنتج')
    description = models.TextField(blank=True, verbose_name='الوصف')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other', verbose_name='الفئة')
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='used', verbose_name='الحالة')
    is_available = models.BooleanField(default=True, verbose_name='متاح للبيع')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name='صورة المنتج')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخر تعديل')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']
