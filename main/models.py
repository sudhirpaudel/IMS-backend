from django.utils import timezone
from django.db import models

# Create your models here.
class Client(models.Model):
  
    client_name = models.CharField(max_length=200)
    client_type = models.CharField(max_length=50,null=True) 
    province = models.CharField(max_length=50,null=True)
    district = models.CharField(max_length=50,null=True)
    municipality = models.CharField(max_length=50,null=True)
    ward_no = models.TextField(max_length=2,null=True)
    address = models.TextField(max_length=50,null=True)
    pan_number = models.CharField(max_length=12,null=True,unique=True)
    manager_name = models.CharField(max_length=50,null=True)
    manager_phone = models.CharField(max_length=10,null=True)
    client_phone = models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.client_name


        
class Product(models.Model):
    
    client= models.ForeignKey(Client,on_delete=models.CASCADE)
    product_type = models.CharField(max_length=20,null=True)
    product_name= models.CharField(max_length=200)
    article_number = models.CharField(max_length=10,null=True,unique=True)
    color = models.CharField(max_length=10,null=True)
    product_category = models.CharField(max_length=50,null=True)
   
    
    def __str__(self):
        return self.product_name




class Transaction(models.Model):
    
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(default=timezone.now) 
    number_of_products = models.IntegerField(null=True)
    total_number_of_products = models.IntegerField(null=True)
    total_amount = models.FloatField(null=True)
    transaction_type = models.CharField(max_length=20,null=True)
    need_vat = models.BooleanField(null=True)
    with_vat = models.BooleanField(null=True)
    def __str__(self):
        client_1 = self.client_id
        mymodel1 = Client.objects.get(id=client_1)
        return mymodel1.client_name



class TransactionProductDetail(models.Model):
    transaction= models.ForeignKey(Transaction,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    number_of_products = models.IntegerField(null=True)
    number_of_sizes = models.IntegerField(null=True)
    need_vat = models.BooleanField(null=True)
    with_vat = models.BooleanField(null=True)
    product_price = models.FloatField(null=True)

    
    def __str__(self):
        return self.transaction_type


class TransactionProductSizeDetail(models.Model):
    transaction= models.ForeignKey(Transaction,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.CharField(max_length=10,null=True)
    number_of_products = models.IntegerField(null=True)
    def __str__(self):
        return self.size




class TotalSizeCount(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.CharField(max_length=20,null=True)
    number_of_products = models.IntegerField(null=True)
    def __str__(self):
        return self.size




class TotalProductCount(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    number_of_products = models.IntegerField(null=True)
    def __str__(self):
        return self.product
