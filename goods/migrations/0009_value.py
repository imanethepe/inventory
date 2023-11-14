# Generated by Django 3.2.5 on 2023-11-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_item_total_item_estimated_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_inventory_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
    ]
