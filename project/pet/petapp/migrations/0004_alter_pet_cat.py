# Generated by Django 5.0.1 on 2024-01-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0003_alter_pet_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Dog'), (2, 'Cat'), (3, 'Bird')]),
        ),
    ]
