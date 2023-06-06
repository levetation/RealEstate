from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

## external imports
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(_("username or company name"), unique=True, max_length=250)
    contact_number = PhoneNumberField(_("contact number"), region='GB', null=True, blank=True)
    
    USER_TYPE_CHOICES = (('buyer', 'Buyer'),('seller', 'Seller'),)
    user_type = models.CharField(_("user type"), max_length=10, choices=USER_TYPE_CHOICES, default="buyer")
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "contact_number", "user_type",]

    objects = CustomUserManager()

    def __str__(self):
        return self.name
    
class UserAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    address1 = models.CharField(
        _("Address line 1"),
        max_length=1024,
        null=True, blank=True
    )

    address2 = models.CharField(
        _("Address line 2"),
        max_length=1024,
        null=True, blank=True
    )

    postcode = models.CharField(
        _("Postcode"),
        max_length=12,
        null=True, blank=True
    )

    city = models.CharField(
        _("City"),
        max_length=1024,
        null=True, blank=True
    )

    county = models.CharField(
        _("County"),
        max_length=1024,
        null=True, blank=True
    )

    def __str__(self):
        return self.address1

class UserLogo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    logo = models.ImageField( _("logo"), upload_to="users/static/users", null=True, blank=True)

    def __str__(self):
        return self.logo.name


