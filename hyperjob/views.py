from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


# Create your views here.

class MenuPageView(View):
    pages = {
        "login": "/login",
        "signup": "/signup",
        "vacancies": "/vacancies",
        "resumes": "/resumes",
        "home": "/menu",
    }

    def get(self, request, *args, **kwargs):
        return render(request, 'menu/main_page.html', {'pages': self.pages})


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    template_name = 'menu/login.html'


class MyLogoutView(LogoutView):
    template_name = 'menu/logged_out.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'menu/signup.html'
