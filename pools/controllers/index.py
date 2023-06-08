from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):

    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def skills(request):
    return render(request, 'skills.html', {})


def personal_account(request):
    return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html', {})


def login(request):
    return render(request, 'login.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


def skills(request):
    return render(request, 'skills.html', {})


