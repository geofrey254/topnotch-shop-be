# Generated by Django 5.1.5 on 2025-03-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_product_main_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_category',
            field=models.CharField(choices=[('Lab Equipment', 'Lab Equipment'), ('Books', 'Books'), ('Technology', 'Technology'), ('Stationery', 'Stationery')], max_length=50, null=True),
        ),
    ]
