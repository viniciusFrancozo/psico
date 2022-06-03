# Generated by Django 4.0.4 on 2022-06-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_remove_account_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='cargo',
            field=models.CharField(choices=[('', 'Cargo'), ('PE', 'Cliente'), ('PI', 'Psicologo')], default='', max_length=15),
        ),
    ]
