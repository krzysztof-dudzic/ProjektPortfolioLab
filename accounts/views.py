from django.shortcuts import render
from django.views import View, generic
from django.contrib.auth import views
# from .forms import RegisterForm
from django.shortcuts import render
from django.views import View, generic
# from charitydonation.models import Donation, Institution
from .forms import CreateUserForm, LoginForm, CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate, views
from django.shortcuts import redirect
from django.urls import reverse_lazy


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            # breakpoint()
            if user is not None:

                login(request, user)
                return redirect('landing-page')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # form.clean_password2()

            # email = form.cleaned_data['email']
            # raw_password = form.cleaned_data['password']
            # user = authenticate(email=email, password=raw_password)
            # user.save()
            # login(request, user)
            return redirect('landing-page')
        return render(request, 'register.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing-page')
