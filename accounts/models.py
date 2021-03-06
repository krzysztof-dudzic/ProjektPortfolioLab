from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, UserManager
)
#
# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         if not password:
#             raise ValueError("Users must have a password!!! ")
#         user = self.model(
#             email=self.normalize_email(email),
#         )
#
#         user.set_password(password)
#         user.staff = is_staff
#         user.admin = is_admin
#         user.active = is_active
#         # user.save(using=self._db)
#         return user
#
#     def create_staffuser(self, email, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         # user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         # user.save(using=self._db)
#         return user
#
# class User(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     # full_name = models.CharField(max_length=255, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False) # a admin user; non super-user
#     admin = models.BooleanField(default=False) # a superuser
#     timestamp = models.DateTimeField(auto_now_add=True)
#     # notice the absence of a "Password field", that is built in.
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [] # Email & Password are required by default.
#     objects = UserManager()
#
#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff
#
#     @property
#     def is_active(self):
#         "Is the user a admin member?"
#         return self.active
#
#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin
#
#
#
#
#
# class GuestEmail(models.Model):
#     email = models.EmailField()
#     active = models.BooleanField(default=True)
#     update = models.DateTimeField(auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.email

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError("Users must have a password!!! ")

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
