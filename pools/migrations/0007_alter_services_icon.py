# Generated by Django 4.2.1 on 2023-06-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0006_alter_services_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.URLField(default='', max_length=500),
        ),
    ]
