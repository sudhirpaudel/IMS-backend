# Generated by Django 4.1.5 on 2023-01-31 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
    ]