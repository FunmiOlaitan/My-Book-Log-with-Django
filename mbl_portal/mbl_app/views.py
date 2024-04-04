from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def library(request):
    return render(request, 'library.html')

def contact(request):
    return render(request, 'contact.html')
