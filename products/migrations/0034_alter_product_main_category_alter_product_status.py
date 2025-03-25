# Generated by Django 5.1.5 on 2025-03-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_alter_product_main_category_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_category',
            field=models.CharField(choices=[('Books', 'Books'), ('Lab Equipment', 'Lab Equipment'), ('Technology', 'Technology'), ('Stationery', 'Stationery')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('PB', 'Published'), ('DT', 'Draft')], default='DT', max_length=2),
        ),
    ]
