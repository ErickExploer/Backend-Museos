# Generated by Django 5.0.6 on 2024-12-23 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_userprofile_email_userprofile_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
    ]
