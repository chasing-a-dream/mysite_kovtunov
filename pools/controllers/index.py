from django.shortcuts import redirect, render


def index(request):

    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def skills(request):
    return render(request, 'skills.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


def skills(request):
    return render(request, 'skills.html', {})


