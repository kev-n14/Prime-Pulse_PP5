# Generated by Django 3.2.21 on 2023-09-12 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_default_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_profile_picture',
        ),
    ]
