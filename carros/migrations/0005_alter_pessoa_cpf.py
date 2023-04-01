# Generated by Django 4.1.7 on 2023-04-01 20:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0004_alter_pessoa_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Digite apenas números.'), django.core.validators.MinLengthValidator(5)]),
        ),
    ]