# Generated by Django 3.2.5 on 2023-11-14 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_total_inventory_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='total_inventory_value',
        ),
        migrations.RemoveField(
            model_name='item',
            name='total_item_estimated_price',
        ),
    ]
