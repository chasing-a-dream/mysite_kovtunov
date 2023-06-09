from django.shortcuts import render
from django.views.generic import ListView
from .models import Services, WhatProvide, Portfolio

def services(request):
    servicesList = Services.objects.all()
    for service in servicesList:
        provides = WhatProvide.objects.filter(service_id=service.id).all()
        setattr(service, 'provides', provides)
    return render(request, "services.html", {'servicesList': servicesList})


class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    queryset = Portfolio.objects.all().order_by('title')
