from rest_framework.serializers import ModelSerializer
from .models import Company,Product,Transaction

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'