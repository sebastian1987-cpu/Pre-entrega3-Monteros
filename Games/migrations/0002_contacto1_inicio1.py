# Generated by Django 4.1.5 on 2023-02-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Inicio1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portada', models.CharField(max_length=30)),
                ('saludo', models.CharField(max_length=30)),
            ],
        ),
    ]