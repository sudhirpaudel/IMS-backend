from django.utils import timezone
from django.db import models

# Create your models here.
class Company(models.Model):
    company_types = (
        ('S', 'Factory'),
        ('M', 'Shop'),
        ('L', 'Deler'),
        ('P','Person')
    )
    municipality_types = (
        ('ME', 'Metropoliton'),
        ('SM', 'Sub-Metro'),
        ('MU', 'Municipality'),
        ('V','VDC')
    )
    company_id= models.CharField(max_length=10)
    company_name = models.CharField(max_length=200)
    company_type = models.CharField(max_length=1, choices=company_types,default='S')
    district = models.CharField(max_length=50,null=True)
    province = models.CharField(max_length=50,null=True)
    municipality_type = models.CharField(max_length=2,choices=municipality_types,null=True)
    municipality = models.CharField(max_length=50,null=True)
    ward_no = models.IntegerField(null=True)
    pan_number = models.CharField(max_length=12,null=True)
    shop_keeper_name = models.CharField(max_length=50,null=True)
    shop_keeper_phone = models.CharField(max_length=10,null=True)
    manager_name = models.CharField(max_length=50,null=True)
    manager_phone = models.CharField(max_length=10,null=True)
    company_phone = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.company_name

class Product(models.Model):
    product_category_types = (('M','Male'),('F','Female'),('K','Kids'))
    company= models.ForeignKey(Company,on_delete=models.CASCADE)
    product_id = models.CharField(max_length=10)
    product_name= models.CharField(max_length=200)
    article_number = models.CharField(max_length=10,null=True)
    color = models.CharField(max_length=10,null=True)
    product_category = models.CharField(max_length=2,choices=product_category_types,null=True)
    product_type = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.product_name


class Transaction(models.Model):
    transaction_types=(('S','Sales'),('P','Purchase'))
    transaction_date = models.DateTimeField(default=timezone.now) 
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    number_of_products = models.IntegerField(null=True)
    transaction_type = models.CharField(max_length=2,choices=transaction_types,null=True)
    
    def __str__(self):
        company_1 = self.company_id
        mymodel1 = Company.objects.get(id=company_1)
        return mymodel1.company_name


