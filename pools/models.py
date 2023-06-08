from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Feedback(models.Model):
    email = models.CharField(max_length=30)
    text = models.TextField()


class Services(models.Model):
    auth_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    service_text = models.TextField()
    icon = models.URLField(max_length=500, default='')
    more_service_name = models.CharField(max_length=100, default='')
    more_service_question = models.CharField(max_length=100, default='')
    more_service_text = models.TextField(default='')

    class Meta:
        ordering = ['service_name']

    def __str__(self):
        return f'{self.service_name}'


class WhatProvide(models.Model):
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    point = models.TextField()

    def __str__(self):
        return f'{self.point} - {self.service_id}'


