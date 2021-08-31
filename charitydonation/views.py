from django.shortcuts import render
from django.views import View, generic
from .models import Donation, Institution
# from .forms import CreateUserForm, LoginForm
from django.contrib.auth import login, logout, authenticate, views
from django.shortcuts import redirect
from django.urls import reverse_lazy


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


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


# class Login(View):
#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'login.html', {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
#             if user is not None:
#                 login(request, user)
#                 return redirect('landing-page')
#                 # return HttpResponse("Jest ok")
#             else:
#                 return render(request, 'login.html', {'form': form})
#         else:
#             return render(request, 'login.html', {'form': form})

# class LoginView(views.LoginView):
#     form_class = LoginForm
#     template_name = 'login.html'
#
#
# class RegisterView(generic.CreateView):
#     form_class = CreateUserForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')


# class Register(View):
#     def get(self, request):
#         form = CreateUserForm()
#         return render(request, 'register.html', {'form': form})
#
#     def post(self, request):
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(email=email, password=raw_password)
#             user.save()
#             login(request, user)
#             return redirect('landing-page')
#         return render(request, 'register.html', {'form': form})
