# Generated by Django 4.1.2 on 2022-10-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_interested_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart_flag',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
