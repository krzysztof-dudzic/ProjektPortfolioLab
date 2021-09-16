"""donation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from charitydonation.views import LandingPage, AddDonation, UserView, PasswordChangeView, PasswordChangeDoneView, DonationReady
from accounts.views import RegisterView, LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='landing-page'),
    path('add_donation/', AddDonation.as_view(), name='add-donation'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_view/', UserView.as_view(), name='user-view'),
    path('password_change/', PasswordChangeView.as_view(), name='user-change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='user-change-done'),
    path('add_donation/form-confirmation/', DonationReady.as_view(), name='form-ready'),


]
