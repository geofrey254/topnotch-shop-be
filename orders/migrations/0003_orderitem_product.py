# Generated by Django 5.1.5 on 2025-02-14 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderitem_book_remove_orderitem_lab_equipment_and_more'),
        ('products', '0008_remove_bookimage_book_remove_device_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]
