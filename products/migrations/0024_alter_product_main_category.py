# Generated by Django 5.1.5 on 2025-03-20 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_product_main_category_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_category',
            field=models.CharField(choices=[('Lab Equipment', 'Lab Equipment'), ('Technology', 'Technology'), ('Books', 'Books'), ('Stationery', 'Stationery')], max_length=50, null=True),
        ),
    ]
