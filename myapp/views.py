from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'About.html')


def services(request):
    return render(request, 'Services.html')


def qw(request):
    first = 't1'
    return render(request, 'Services.html')


def contact(request):
    return render(request, 'Contact Us.html')


def abc(request):
    return render(request, 'Services.html')
