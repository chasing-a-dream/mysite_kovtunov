from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html', {})


def about(request):
    name = request.GET.get('name')
    return render(request, 'about.html', {'name': name,
                                          'title': "обо мне"})


def about_work(request):
    return HttpResponse("Software engineer")


def contacts(request):
    return render(request, 'contacts.html', {})


def hobbies(request):
    return HttpResponse("Увлечения")

def gallery(request):
    return HttpResponse("Photo")