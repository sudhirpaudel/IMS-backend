from django.contrib import admin
from .models import Client,Product,Transaction,TransactionProductDetail,TransactionProductSizeDetail,TotalSizeCount,TotalProductCount
# Register your models here.


admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(TransactionProductDetail)
admin.site.register(TransactionProductSizeDetail)
admin.site.register(TotalSizeCount)
admin.site.register(TotalProductCount)