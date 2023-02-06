from django.contrib import admin
from .models import Client,Product,Transaction,TransactionProductDetail,TransactionProductSizeDetail
# Register your models here.


admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(TransactionProductDetail)
admin.site.register(TransactionProductSizeDetail)