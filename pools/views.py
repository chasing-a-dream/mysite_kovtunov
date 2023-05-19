from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


