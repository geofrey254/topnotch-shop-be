# Generated by Django 5.1.5 on 2025-03-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_shipping_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_reference',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
