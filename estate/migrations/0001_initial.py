# Generated by Django 3.2.8 on 2021-10-30 10:52

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100, null=True)),
                ('occupant_count', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField(null=True)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('neighourhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estate.neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('business_image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='business')),
                ('location', models.CharField(blank=True, max_length=225, null=True)),
                ('business_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estate.neighborhood')),
                ('business_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
