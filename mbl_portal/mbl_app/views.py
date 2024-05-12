from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserLoginForm, UserRegistrationForm

# Define views for login, logout, and registration
class UserLoginView(LoginView):
    template_name = 'login.html'  # Set the template for login
    authentication_form = UserLoginForm  # Set the authentication form

class UserLogoutView(LogoutView):
    next_page = '/'  # Redirect to the home page after logout

class UserRegistrationView(CreateView):
    template_name = 'registration.html'  # Set the template for registration
    form_class = UserRegistrationForm  # Set the registration form
    success_url = reverse_lazy('login')  # Redirect to the login page after successful registration

# Define additional views for profile, library, and contact pages

def profile(request):
    return render(request, 'profile.html')

def library(request):
    return render(request, 'library.html')

def contact(request):
    return render(request, 'contact.html')

def registration(request):
    return render(request, 'registration.html')