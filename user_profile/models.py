from django.conf import settings
from django.db import models

from orders.countries import Countries

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/%Y/%m')
    address_line_1 = models.CharField(max_length=255, default="")
    address_line_2 = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    state_province_region = models.CharField(max_length=255, default="")
    zipcode = models.CharField(max_length=20, default="")
    phone = models.CharField(max_length=255, default="")
    country_region = models.CharField(
        max_length=255, choices=Countries.choices, default=Countries.Canada
    )

    def __str__(self):
        return self.user
