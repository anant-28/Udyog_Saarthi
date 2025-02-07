# Generated by Django 4.2.6 on 2023-10-10 18:32

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
            name='CandidateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mothers_name', models.CharField(blank=True, max_length=255)),
                ('fathers_name', models.CharField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True)),
                ('pincode', models.IntegerField(max_length=6)),
                ('DOB', models.DateField()),
                ('stream', models.CharField(max_length=100)),
                ('UDID', models.IntegerField()),
                ('functional_difficulties', models.TextField(max_length=200)),
                ('assistive_device', models.CharField(max_length=100)),
                ('human_assistance', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
