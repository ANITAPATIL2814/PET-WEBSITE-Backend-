# Generated by Django 5.0.1 on 2024-01-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0006_alter_cart_pid_alter_cart_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]