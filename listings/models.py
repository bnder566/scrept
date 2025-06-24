from django.db import models
from django.utils.translation import gettext_lazy as _

class Listing(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', _('قيد المراجعة')
        APPROVED = 'approved', _('مقبول')
        REJECTED = 'rejected', _('مرفوض')

    title = models.CharField(max_length=100, verbose_name=_("عنوان"))
    description = models.TextField(verbose_name=_("الوصف"))
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("السعر"),
        default=0.00  # ✅ القيمة الافتراضية
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإضافة"))
    
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
        verbose_name=_("الحالة")
    )

    class Meta:
        verbose_name = _("إعلان")
        verbose_name_plural = _("الإعلانات")

    def __str__(self):
        return self.title
