from django.shortcuts import render
from django.views import View, generic
from .models import Donation, Institution, Category
from .forms import AddDonationForm
from django.contrib.auth import login, logout, authenticate, views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView
from django.db.models import Avg, Count
from django.core.paginator import Paginator
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.http import HttpResponse
from django.db.models import Q, Sum


class LandingPage(View):
    def get(self, request):
        count_bags = Donation.objects.all()
        count_b = count_bags.aggregate(Sum('quantity'))['quantity__sum']
        count_institutions = Donation.objects.distinct("institution").count()


        #
        all_institution_fund = Institution.objects.filter(type='1')
        all_institution_org = Institution.objects.filter(type='2')
        all_institution_lok = Institution.objects.filter(type='3')

        return render(request, 'index.html', {'count_b': count_b, 'count_institutions': count_institutions,
                                              'all_institution_fund': all_institution_fund,
                                              'all_institution_org': all_institution_org,
                                              'all_institution_lok': all_institution_lok}
                      )


class AddDonation(LoginRequiredMixin, View):
    login_url = '/'
    # raise_exception = True

    def get(self, request):
        categories_all = Category.objects.all()
        institutions_all = Institution.objects.all()
        form = AddDonationForm()

        # redirect_field_name = 'landing-page'
        return render(request, 'form.html',
                      {'categories_all': categories_all,
                       'institutions_all': institutions_all, 'form': form})

    def post(self, request):
        form = AddDonationForm(request.POST)

        if form.is_valid():

            # categories_all = Category.objects.all()
            categories = form.cleaned_data['categories']
            # institutions_all = Institution.objects.all()
            quantity = form.cleaned_data['bags']
        # category_id = request.POST.get('category.id')
        # catogeria = Institution.objects.filter(id=category_id)
            institution = form.cleaned_data['organization']
        # if request.POST.get(
        #     catego = Category.objects.get(id=category_id)
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['postcode']
            phone_number = form.cleaned_data['phone']
            pick_up_date = form.cleaned_data['data']
            pick_up_time = form.cleaned_data['time']
            pick_up_comment = form.cleaned_data['more_info']
            user = request.user
            donat = Donation.objects.create(
                quantity=quantity, categories=categories, institution=institution,
                address=address, phone_number=phone_number, city=city, zip_code=zip_code,
                pick_up_date=pick_up_date, pick_up_comment=pick_up_comment, pick_up_time=pick_up_time,
                user=user)
            donat.save()
        # redirect_field_name = 'landing-page'
            return render(request, 'form-confirmation.html', {'form': form})

        return render(request, 'form.html', {'form': form})
            # return HttpResponse("Źle")
# class LoginView(views.LoginView):
#     form_class = LoginForm
#     template_name = 'login.html'
#
#
# class RegisterView(generic.CreateView):
#     form_class = CreateUserForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')


class UserView(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request):
        donation_user = Donation.objects.filter(user=request.user)
        return render(request, 'user-view.html', {'donation_user': donation_user})


class PasswordChangeView(PasswordChangeView):
    template_name = 'change-password.html'
    success_url = 'done/'


class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'change-password-done.html'


class DonationReady(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')
