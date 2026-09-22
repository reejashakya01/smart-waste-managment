from django.db import models

# Create your models here.
from django.db import models
from apps.accounts.models import User

# Create your models here.
class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=200, null=True, blank=True)
    address_line = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.address_line}'

    class Meta:
        db_table = "Useraddress"