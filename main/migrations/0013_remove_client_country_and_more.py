# Generated by Django 4.1.5 on 2023-01-31 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_client_producttype_remove_product_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='country',
        ),
        migrations.RemoveField(
            model_name='client',
            name='municipality_type',
        ),
        migrations.RemoveField(
            model_name='client',
            name='shop_keeper_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='shop_keeper_phone',
        ),
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
