
from main.models import Client, Product,Transaction,TransactionProductDetail,TransactionProductSizeDetail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClientSerializer , ProductSerializer,TransactionSerializer,TransactionProductDetailSerializer,TransactionProductSizeDetailSerializer

@api_view(['POST'])
def create_client(request):
    data = request.data
    client = Client.objects.create(
        client_name = data['client_name'],
        client_type = data['client_type'],
        pan_number = data['pan_number'], 
        province = data['province'],
        district = data['district'],
        address = data['address'],
        municipality = data['municipality'],
        ward_no = data['ward_no'],
        manager_name = data['manager_name'],
        manager_phone = data['manager_phone'],
        client_phone = data['client_phone'],
        email = data['email']
    )
    serializer = ClientSerializer(client,many=False)
    return  Response(serializer.data)


@api_view(['GET'])
def get_client_all(request):
    clients= Client.objects.all()
    serializer = ClientSerializer(clients,many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def get_client(request,id):
    client =Client.objects.get(id=id)
    serializer =ClientSerializer(client,many=False)
    return  Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    data = request.data
    product = Product.objects.create(
        client= Client.objects.get(client_name = data['client_name']),
        product_name= data['product_name'],
        article_number = data['article_number'],
        color = data['color'],
        product_category = data['product_category'],
        product_type =data['product_type'],
       
    )
    serializer = ProductSerializer(product,many=False)
    return  Response(serializer.data)


@api_view(['GET'])
def get_product_all(request):
    products= Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def get_product(request,id):
    product= Product.objects.get(id = id)
    serializer = ProductSerializer(product,many=False)
    return  Response(serializer.data)





@api_view(['POST'])
def create_transaction(request):
    data = request.data
    transaction = Transaction.objects.create(
        client= Client.objects.get(id=data['client']),
        product =Product.objects.get(id =data['product']),
        transaction_date = data['transaction_date'],
        number_of_products = data['number_of_products'],
        total_number_of_products  = data['total_number_of_products'],
        total_amount=data['total_amount']
    
    )
    serializer = TransactionSerializer(transaction,many=False)
    return  Response(serializer.data)


@api_view(['GET'])
def get_transaction_all(request):
    transactions= Transaction.objects.all()
    serializer = TransactionSerializer(transactions,many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def get_transaction(request,id):
    transaction= Transaction.objects.get(id = id)
    serializer =TransactionSerializer(transaction,many=False)
    return  Response(serializer.data)




