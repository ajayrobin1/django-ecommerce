# Generated by Django 4.1.2 on 2022-10-21 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_interested_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='interested_users',
        ),
    ]
