from django.db import models
from django.utils.translation import gettext_lazy as _

class Location(models.Model):
    city = models.CharField(max_length=100, verbose_name=_("المدينة"))

    class Meta:
        verbose_name = _("موقع")
        verbose_name_plural = _("المواقع")

    def __str__(self):
        return self.city
