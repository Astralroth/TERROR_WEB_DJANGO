# Generated by Django 3.2.3 on 2021-06-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=256, null=True)),
                ('last_name', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True, unique=True, verbose_name='Correo electronico')),
                ('run', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=9, null=True)),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('movie_preference', models.CharField(blank=True, max_length=30, null=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True)),
                ('is_anonymous', models.BooleanField()),
                ('is_authenticated', models.BooleanField()),
            ],
        ),
    ]
