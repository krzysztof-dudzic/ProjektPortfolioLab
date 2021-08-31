from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

#
# class LoginForm(AuthenticationForm):
#     email = forms.CharField(max_length=64, label="Email")
    # password = forms.CharField(widget=forms.PasswordInput, label='Hasło')


# class CreateUserForm(forms.ModelForm):
#     username = forms.CharField(max_length=12)
#     password = forms.CharField(max_length=16, label="Hasło", widget=forms.PasswordInput)
#     password2 = forms.CharField(max_length=16, label="Powtórz hasło", widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2', ]
#
#     def clean(self):
#         clean_data = self.cleaned_data
#         pas1 = clean_data['password']
#         pas2 = clean_data['password2']
#         if pas1 != pas2:
#             raise ValidationError('Passwords are incorrect')
#

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'username', 'password1', 'password2')
