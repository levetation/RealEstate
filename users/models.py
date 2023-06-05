from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )

    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(_("username or company name"), unique=True, max_length=250)
    contact_number = PhoneNumberField(_("contact number"), region='GB', null=True, blank=True)
    user_type = models.CharField(_("user type"), max_length=10, choices=USER_TYPE_CHOICES, default="buyer")
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "user_type", "contact_number"]

    objects = CustomUserManager()

    def __str__(self):
        return self.name
