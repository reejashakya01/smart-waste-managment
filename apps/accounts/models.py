from django.db import models
from django.contrib.auth.models import AbstractUser,  UserManager
# Create your models here.

class Role(models.TextChoices):
    ADMIN = "admin"
    CUSTOMER = "customer"
    COLLECTOR = "collector"

class CustomManager(UserManager):

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('role',Role.ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    phone_number = models.PositiveBigIntegerField(unique=True)
    alternative_number = models.PositiveBigIntegerField(null=True,blank=True)
    reward_point = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    role = models.CharField(max_length=30, choices=Role.choices, default=Role.CUSTOMER)
    email = models.EmailField(unique=True)

    objects = CustomManager()
    REQUIRED_FIELDS = ['email','phone_number']
    
    