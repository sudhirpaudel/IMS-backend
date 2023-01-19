from django.urls import path
from . import views


urlpatterns=[
    path('company/add',views.create_company,name='create_company'),
    path('company',views.get_company_all,name='View ALl Companies'),
    path('company/<int:id>',views.get_company,name='View Company'),


    path('product',views.get_product_all,name='View All Products'),
    path('product/<int:id>',views.get_product,name='View Product'),
    path('product/add',views.create_product,name='Create Product'),


    path('transaction',views.get_transaction_all,name='View All Transactions'),
    path('transaction/<int:id>',views.get_transaction,name='View transaction'),
    path('transaction/add',views.create_transaction,name='Create transaction'),

]