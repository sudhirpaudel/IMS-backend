# Generated by Django 4.1.5 on 2023-01-31 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rename_emial_client_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=10)),
                ('product_name', models.CharField(max_length=200)),
                ('article_number', models.CharField(max_length=10, null=True, unique=True)),
                ('color', models.CharField(max_length=10, null=True)),
                ('product_category', models.CharField(max_length=50, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producttype')),
            ],
        ),
    ]
