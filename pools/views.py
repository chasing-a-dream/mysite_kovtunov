from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Services, WhatProvide


class ServicesListView(ListView):
    model = Services
    template_name = 'services.html'


class WhatProvideListView(ListView):
    model = WhatProvide
    template_name = 'services.html'

# def PkComparison(pk1, pk2):
#     if pk1 == pk2
#         re