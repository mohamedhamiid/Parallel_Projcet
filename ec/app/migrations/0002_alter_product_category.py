# Generated by Django 5.0.4 on 2024-04-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CZ', 'Cheese'), ('CR', 'Curd'), ('ML', 'Milk'), ('GH', 'Ghee'), ('PN', 'Paneer'), ('MS', 'Milkshake'), ('IC', 'Ice-Creams'), ('LS', 'Lassi')], max_length=2),
        ),
    ]
