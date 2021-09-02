from django.shortcuts import render
from django.views import View, generic
from .models import Donation, Institution
# from .forms import CreateUserForm, LoginForm
from django.contrib.auth import login, logout, authenticate, views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView



class LandingPage(View):
    def get(self, request):
        count_bags = Donation.objects.count()
        count_institutions = Institution.objects.count()
        all_institution_fund = Institution.objects.filter(type="Fundacja")
        all_institution_org = Institution.objects.filter(type="Organizacja pozarządowa")
        all_institution_lok = Institution.objects.filter(type="Zbiórka lokalna")

        return render(request, 'index.html', {'count_bags': count_bags, 'count_institutions': count_institutions,
                                              'all_institution_fund': all_institution_fund,
                                              'all_institution_org': all_institution_org,
                                              'all_institution_lok': all_institution_lok})


class AddDonation(LoginRequiredMixin, View):
    login_url = '/'
    # raise_exception = True
    def get(self, request):

        # redirect_field_name = 'landing-page'
        return render(request, 'form.html')




# class LoginView(views.LoginView):
#     form_class = LoginForm
#     template_name = 'login.html'
#
#
# class RegisterView(generic.CreateView):
#     form_class = CreateUserForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')



