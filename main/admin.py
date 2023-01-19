from django.contrib import admin
from .models import Company,Product,Transaction
# Register your models here.


admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Transaction)