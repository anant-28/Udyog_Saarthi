# Generated by Django 4.2.6 on 2023-10-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UdyogSaarthi', '0004_pyqs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyqs',
            name='pdf',
            field=models.FileField(upload_to='files/'),
        ),
    ]
