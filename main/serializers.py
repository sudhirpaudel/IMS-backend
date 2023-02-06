from rest_framework.serializers import ModelSerializer
from .models import Client ,Product,Transaction,TransactionProductDetail,TransactionProductSizeDetail

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