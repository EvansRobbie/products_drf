from rest_framework.serializers import ModelSerializer
from .models import Customer, Product

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_imageUrl',
            'get_thumbnail'
        )