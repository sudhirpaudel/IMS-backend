# Generated by Django 4.1.5 on 2023-01-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_company_company_phone_company_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_type',
            field=models.CharField(choices=[('S', 'Factory'), ('M', 'Shop'), ('L', 'Deler'), ('P', 'Person')], default='S', max_length=1),
        ),
    ]