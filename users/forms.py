from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, UserAddress, UserLogo

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(
        label="User Type",
        choices=CustomUser.USER_TYPE_CHOICES,
        initial='buyer',
    )

    class Meta:
        model = CustomUser
        fields = ("email", "name", "contact_number", "user_type")

class CustomUserChangeForm(UserChangeForm):
    user_type = forms.ChoiceField(
        label="User Type",
        choices=CustomUser.USER_TYPE_CHOICES,
    )

    class Meta:
        model = CustomUser
        fields = ("email", "name", "contact_number", "user_type")

class CustomUserAddAddressForm:
    class Meta:
        model = UserAddress
        fields = ("address1", "address2", "postcode", "city", "county")

class CustomUserAddLogoForm:
    class Meta:
        model = UserLogo
        fields = ("logo")
