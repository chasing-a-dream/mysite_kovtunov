# Generated by Django 4.2.1 on 2023-06-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0004_whatprovide_delete_what_i_provide'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['service_name']},
        ),
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.ImageField(upload_to=''),
        ),
    ]
