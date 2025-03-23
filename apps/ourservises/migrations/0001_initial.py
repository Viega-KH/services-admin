# Generated by Django 4.2 on 2025-03-23 10:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ourservises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('title_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('content_uz', models.TextField(blank=True, null=True)),
                ('content_en', models.TextField(blank=True, null=True)),
                ('content_ru', models.TextField(blank=True, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Our Servises',
                'verbose_name_plural': 'Our Servises',
                'ordering': ('-publish',),
            },
        ),
    ]
