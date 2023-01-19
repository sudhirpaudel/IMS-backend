# Generated by Django 4.1.5 on 2023-01-18 13:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_company_company_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='manager_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='manager_phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='municipality',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='municipality_type',
            field=models.CharField(choices=[('ME', 'Metropoliton'), ('SM', 'Sub-Metro'), ('MU', 'Municipality'), ('V', 'VDC')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='pan_number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='province',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='shop_keeper_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='shop_keeper_phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='ward_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='article_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('K', 'Kids')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_type',
            field=models.CharField(choices=[('S', 'Factory'), ('M', 'Shop'), ('L', 'Deler')], default='S', max_length=1),
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('number_of_products', models.IntegerField(null=True)),
                ('transaction_type', models.CharField(choices=[('S', 'Sales'), ('P', 'Purchase')], max_length=2, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]