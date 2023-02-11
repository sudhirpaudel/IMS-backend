from rest_framework.serializers import ModelSerializer
from .models import Client ,Product,Transaction,TransactionProductDetail,TransactionProductSizeDetail,TotalSizeCount,TotalProductCount

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionProductDetailSerializer(ModelSerializer):
    class Meta:
        model = TransactionProductDetail
        fields = '__all__'



class TransactionProductSizeDetailSerializer(ModelSerializer):
    class Meta:
        model = TransactionProductSizeDetail
        fields = '__all__'

class ClientImpSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields= ['id','client_name','pan_number']

class TransactionClientSerializer(ModelSerializer):
    client = ClientImpSerializer(many=False)

    class Meta:
        model = Transaction
        fields = [ "id","transaction_date","number_of_products","total_number_of_products","total_amount","transaction_type","client"]




class TotalSizeCountSerializer(ModelSerializer):
    class Meta:
        model = TotalSizeCount
        fields = '__all__'


class TotalProductCountSerializer(ModelSerializer):
    class Meta:
        model = TotalProductCount
        fields = '__all__'