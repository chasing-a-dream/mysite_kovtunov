# Generated by Django 4.2.1 on 2023-05-30 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0003_services_more_service_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatProvide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.TextField()),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pools.services')),
            ],
        ),
        migrations.DeleteModel(
            name='What_i_provide',
        ),
    ]
