# Generated by Django 5.0.7 on 2024-07-26 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_order_food_orderfood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfood',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
    ]
