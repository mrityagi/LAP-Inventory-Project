# Generated by Django 2.0.2 on 2020-11-24 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0006_inventory_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='price',
        ),
    ]
