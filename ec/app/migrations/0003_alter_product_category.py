# Generated by Django 5.0.4 on 2024-04-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IC', 'Ice-Creams'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('CR', 'Curd'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese')], max_length=2),
        ),
    ]
