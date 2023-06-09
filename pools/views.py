from django.shortcuts import render

from .models import Services, WhatProvide

def services(request):
    servicesList = Services.objects.all()
    for service in servicesList:
        provides = WhatProvide.objects.filter(service_id=service.id).all()
        setattr(service, 'provides', provides)
    return render(request, "services.html", {'servicesList': servicesList})
