# Generated by Django 4.1.2 on 2022-10-26 15:54

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=''),
        ),
    ]
