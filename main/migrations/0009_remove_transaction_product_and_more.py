# Generated by Django 4.1.5 on 2023-01-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='product',
        ),
        migrations.AddField(
            model_name='transaction',
            name='total_number_of_products',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transactionproductdetail',
            name='number_of_sizes',
            field=models.IntegerField(null=True),
        ),
    ]
