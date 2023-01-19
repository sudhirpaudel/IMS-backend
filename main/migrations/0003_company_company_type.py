# Generated by Django 4.1.5 on 2023-01-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_company_id_product_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='S', max_length=1),
        ),
    ]