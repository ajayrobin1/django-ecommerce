# Generated by Django 4.1.2 on 2022-10-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]