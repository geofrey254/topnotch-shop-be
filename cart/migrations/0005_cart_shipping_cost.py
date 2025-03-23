# Generated by Django 5.1.5 on 2025-03-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cartitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shipping_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
