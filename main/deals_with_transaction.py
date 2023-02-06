from main.models import Client,Product,Transaction,TransactionProductDetail,TransactionProductSizeDetail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionSerializer

@api_view(['POST'])
def deal_with_transaction(request):
    data = request.data
    transaction = Transaction.objects.create(
        client= Client.objects.get(id=data['client_id']),
        total_amount=data['total_amount'],
        number_of_products = data['number_of_products'],
        total_number_of_products = data['total_number_of_products'],
        transaction_type = data['transaction_type']
     )
    for i in data['product_detail']:
        transaction_product_detail = TransactionProductDetail.objects.create(
            transaction= transaction,
            product= Product.objects.get(id=i['id']),
            number_of_products = i['number_of_products'],
            number_of_sizes = i['number_of_sizes'],
            transaction_type = data['transaction_type'],
            need_vat =i['need_vat'],
            with_vat = i['with_vat'],
            product_price = i['product_price']
        )
        
        for j in i['size_detail']:
            transaction_product_size_detail= TransactionProductSizeDetail.objects.create(
                transaction= transaction,
                product = Product.objects.get(id=i['id']),
                size = j['size'],
                number_of_product = j['number_of_product']
            )



    serializerMain = TransactionSerializer(transaction,many=False)
    return  Response(serializerMain.data)



