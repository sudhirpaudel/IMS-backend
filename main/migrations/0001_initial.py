# Generated by Django 4.1.5 on 2023-01-17 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=10)),
                ('company_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=10)),
                ('product_name', models.CharField(max_length=200)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company')),
            ],
        ),
    ]
