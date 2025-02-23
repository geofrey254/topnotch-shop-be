# Generated by Django 5.1.5 on 2025-02-17 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_bookimage_book_remove_device_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_category',
            field=models.CharField(choices=[('Books', 'Books'), ('Technology', 'Technology'), ('Stationery', 'Stationery'), ('Lab Equipment', 'Lab Equipment')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product'),
        ),
    ]
