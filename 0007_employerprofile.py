# Generated by Django 4.2.6 on 2023-10-15 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UdyogSaarthi', '0006_alter_pyqs_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='employerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(blank=True, max_length=255)),
                ('organization_address', models.TextField(blank=True)),
                ('organization_type', models.CharField(choices=[('Private', 'Private'), ('Government', 'Government'), ('PSU', 'PSU')], max_length=10)),
                ('pincode', models.IntegerField()),
                ('DOB', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
