from django.urls import path
from . import views,deals_with_transaction


urlpatterns=[
    path('client/add',views.create_client,name='create_client'),
    path('client',views.get_client_all,name='View ALl Clients'),
    path('client/<int:id>',views.get_client,name='View Client'),


    path('product',views.get_product_all,name='View All Products'),
    path('product/<int:id>',views.get_product,name='View Product'),
    path('product/add',views.create_product,name='Create Product'),


    path('transaction',views.get_transaction_all,name='View All Transactions'),
    path('transaction/<int:id>',views.get_transaction,name='View transaction'),
    path('transaction/add',views.create_transaction,name='Create transaction'),




    path('transaction',deals_with_transaction.deal_with_transaction,name='All Transaction Detail Main'),
    path('transactions',deals_with_transaction.get_all_transactions,name='All Transaction Detail Show'),

    path('inventory/',deals_with_transaction.show_inventory,name='All Size Detail'),
    path('transaction/alldetails/<int:id>',deals_with_transaction.get_all_transactions_details,name='All details of transaction')
]