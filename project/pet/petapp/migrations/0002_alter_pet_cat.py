# Generated by Django 5.0.1 on 2024-01-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='cat',
            field=models.CharField(choices=[(1, 'Dog'), (2, 'Cat'), (3, 'Bird')], max_length=50),
        ),
    ]
