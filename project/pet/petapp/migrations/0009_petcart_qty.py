# Generated by Django 5.0.1 on 2024-01-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0008_rename_cart_petcart_remove_pet_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='petcart',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
