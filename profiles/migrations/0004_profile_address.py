# Generated by Django 4.1.2 on 2022-10-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]