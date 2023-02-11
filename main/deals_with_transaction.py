from main.models import Client,Product,Transaction,TransactionProductDetail,TransactionProductSizeDetail,TotalSizeCount,TotalProductCount
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionProductDetailSerializer, TransactionProductSizeDetailSerializer, TransactionSerializer,TotalSizeCountSerializer,TransactionClientSerializer,TotalProductCountSerializer
from django.http import JsonResponse

@api_view(['POST'])
def deal_with_transaction(request):
    data = request.data
    transaction = Transaction.objects.create(
        client= Client.objects.get(client_name = data['client_name']),
        total_amount=data['total_amount'],
        number_of_products = data['number_of_products'],
        total_number_of_products = data['total_number_of_products'],
        transaction_type = data['transaction_type'],
        transaction_date = data['transaction_date'],
        need_vat =data['need_vat'],
        with_vat = data['with_vat'],

     )
    for i in data['product_detail']:
        transaction_product_detail = TransactionProductDetail.objects.create(
            transaction= transaction,
            product= Product.objects.get(product_name=i['product_name']),
            number_of_products = i['number_of_products'],
            number_of_sizes = i['number_of_sizes'],
            product_price = i['product_price']
        )
        
        pproducts_data = TotalProductCount.objects.filter(product=transaction_product_detail.product)
        
        if pproducts_data:
            pproduct_data=pproducts_data[0]
            if data['transaction_type']=='PURCHASE':
                pproduct_data.number_of_products = pproduct_data.number_of_products+i['number_of_products']
            else:
                pproduct_data.number_of_products = pproduct_data.number_of_products-i['number_of_products'] 
            pproduct_data.save()  
        else :
            TotalProductCount.objects.create(product=transaction_product_detail.product,number_of_products=i['number_of_products'])

        for j in i['size_detail']:
            if j['number_of_products'] != 0:
                
                transaction_product_size_detail= TransactionProductSizeDetail.objects.create(
                    transaction= transaction,
                    product = Product.objects.get(product_name=i['product_name']),
                    size = j['size'],
                    number_of_products = j['number_of_products'])
                products_data = TotalSizeCount.objects.filter(product=transaction_product_size_detail.product,size=j['size'])
                if products_data:
                    product_data=products_data[0]
                    if data['transaction_type']=='PURCHASE':
                        product_data.number_of_products = product_data.number_of_products+j['number_of_products']
                    else:
                        product_data.number_of_products = product_data.number_of_products+j['number_of_products']
                    product_data.save()  
                else :
                    TotalSizeCount.objects.create(product=transaction_product_size_detail.product,size=j['size'],number_of_products=j['number_of_products'])
                
                
            



    serializerMain = TransactionSerializer(transaction,many=False)
    return  Response(serializerMain.data)



 

@api_view(['GET'])
def show_inventory(request):
    transcations = TotalProductCount.objects.all()
    serializer = TotalProductCountSerializer(transcations,many=True)
    # transactions= Transaction.objects.all()
    # serializer = TransactionClientSerializer(transactions,many=True)
    # for i in serializer.data:
        
    #     transactionProducts=TransactionProductDetail.objects.filter(transaction_id=i['id'])
    #     serializerP = TransactionProductDetailSerializer(transactionProducts,many=True)
    #     for j in serializerP.data:
            
    #         transactionProductsSize=TransactionProductSizeDetail.objects.filter(transaction_id=i['id'],product_id=j["product"])
    #         serializerPS = TransactionProductSizeDetailSerializer(transactionProductsSize,many=True)
    #         data={
    #             "transaction":serializer.data,
    #             "prod":serializerP.data,
    #             "size":serializerPS.data
    #         }
    return  Response(serializer.data )



@api_view(['GET'])
def get_all_transactions(request):
    
    transactions= Transaction.objects.all()
    serializer = TransactionClientSerializer(transactions,many=True)
    # for i in serializer.data:
        
    #     transactionProducts=TransactionProductDetail.objects.filter(transaction_id=i['id'])
    #     serializerP = TransactionProductDetailSerializer(transactionProducts,many=True)
    #     for j in serializerP.data:
            
    #         transactionProductsSize=TransactionProductSizeDetail.objects.filter(transaction_id=i['id'],product_id=j["product"])
    #         serializerPS = TransactionProductSizeDetailSerializer(transactionProductsSize,many=True)
    #         data={
    #             "transaction":serializer.data,
    #             "prod":serializerP.data,
    #             "size":serializerPS.data
    #         }
    return  Response(serializer.data )

@api_view(['GET'])
def get_all_transactions_details(request,id):
    
    transactions= Transaction.objects.get(id=id)
    serializer = TransactionClientSerializer(transactions,many=False)
    transactionsProducts = TransactionProductDetail.objects.filter(transaction_id=id)
    serializerP = TransactionProductDetailSerializer(transactionsProducts,many=True)
    product= []
    
    for i in serializerP.data:
        print(i)
        productSize = TransactionProductSizeDetail.objects.filter(product_id=i['product'],transaction_id = id)
        serializerS = TransactionProductSizeDetailSerializer(productSize,many=True)
        product1={
            "product":i,
            "sizes":serializerS.data
        }
        product.append(product1)
    data={
        "transaction":serializer.data,
        "products":product
    }
    return  Response(data)