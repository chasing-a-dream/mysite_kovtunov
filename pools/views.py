from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'pools/templates/register.html'
    success_url = reverse_lazy('login')
