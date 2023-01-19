
from main.models import Company,Product,Transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompanySerializer,ProductSerializer,TransactionSerializer

@api_view(['POST'])
def create_company(request):
    data = request.data
    company = Company.objects.create(
        company_id=data['company_id'],
        company_name = data['company_name'],
        company_type = data['company_type'],
        district = data['district'],
        province = data['province'],
        municipality_type = data['municipality_type'],
        municipality = data['municipality'],
        ward_no = data['ward_no'],
        pan_number = data['pan_number'],
        shop_keeper_name = data['shop_keeper_name'],
        shop_keeper_phone = data['shop_keeper_phone'],
        manager_name = data['manager_name'],
        manager_phone = data['manager_phone'],
        company_phone = data['company_phone'],
    )
    serializer = CompanySerializer(company,many=False)
    return  Response(serializer.data)


@api_view(['GET'])
def get_company_all(request):
    companies= Company.objects.all()
    serializer = CompanySerializer(companies,many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def get_company(request,id):
    company =Company.objects.get(id=id)
    serializer =CompanySerializer(company,many=False)
    return  Response(serializer.data)



@api_view(['POST'])
def create_product(request):
    data = request.data
    product = Product.objects.create(
        company= Company.objects.get(id=data['company']),
        product_id = data['product_id'],
        product_name= data['product_name'],
        article_number = data['article_number'],
        color = data['color'],
        product_category = data['product_category'],
        product_type =data['product_type']
    
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
        company= Company.objects.get(id=data['company']),
        product =Product.objects.get(id =data['product']),
        transaction_date = data['transaction_date'],
        number_of_products = data['number_of_products'],
        transaction_type = data['transaction_type']
    
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