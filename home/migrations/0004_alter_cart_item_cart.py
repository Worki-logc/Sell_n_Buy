# Generated by Django 4.2.16 on 2024-11-04 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_cart_cart_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='home.cart'),
        ),
    ]
