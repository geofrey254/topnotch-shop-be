# Generated by Django 5.1.5 on 2025-03-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_product_main_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_category',
            field=models.CharField(choices=[('Stationery', 'Stationery'), ('Lab Equipment', 'Lab Equipment'), ('Books', 'Books'), ('Technology', 'Technology')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('PB', 'Published'), ('DT', 'Draft')], default='DT', max_length=2),
        ),
    ]
