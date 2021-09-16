import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# from ProjektPortfolioLab.donation import settings
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

INSTITUTIONS = (
    ('1', "Fundacja"),
    ('2', "Organizacja pozarządowa"),
    ('3', "Zbiórka lokalna"),
)


class Institution(models.Model):

    istitution_name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(max_length=2, choices=INSTITUTIONS, default='1')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.istitution_name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=64)
    zip_code = models.TextField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField(default=datetime.time)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#
# class CustomUser(AbstractUser):
#     email = models.EmailField(_('email address'), unique=True)

