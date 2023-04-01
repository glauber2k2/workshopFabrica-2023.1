# Generated by Django 4.1.7 on 2023-04-01 20:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id_pessoa', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id_carro', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=255)),
                ('problema', models.CharField(max_length=255)),
                ('placa', models.CharField(max_length=7)),
                ('pessoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carros.pessoa')),
            ],
        ),
    ]
