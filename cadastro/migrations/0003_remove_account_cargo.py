# Generated by Django 4.0.4 on 2022-06-02 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_account_cargo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='cargo',
        ),
    ]
