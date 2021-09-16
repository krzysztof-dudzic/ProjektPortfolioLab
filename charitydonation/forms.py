from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Donation
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'username', 'password1', 'password2')


class AddDonationForm(forms.Form):
    class Meta:
        model = Donation
        fields = ('quantity', 'categories', 'institution', 'address', 'phone_number',
                  'city', 'zip_code', 'pick_up_date', 'pick_up_time', 'pick_up_comment', 'user')
