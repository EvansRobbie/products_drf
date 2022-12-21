from django.http import Http404
from .serializers import CustomerSerializer, ProductSerializers
from .models import Customer, Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

@api_view(['GET'])
def customer_api(request, *args, **kwargs):
    instance = Customer.objects.all()

    serializer = CustomerSerializer(instance, many = True)
    
    return Response(serializer.data)

@api_view(['GET'])
def LatestProductsList(request, *args, ** kwargs):
    instance = Product.objects.all()[0:4]

    serializer = ProductSerializers(instance, many = True)

    return Response(serializer.data)
# Create your views here.
class ProductDetail(APIView):
    def get_object(self,category_slug, product_slug):
        try:
            return Product.objects.filter(category_slug = category_slug).get(product_slug = product_slug)
        except Product.DoesNotExist:
            raise Http404
    def get(self, category_slug, product_slug, format = None):
        instance = self.get_object(category_slug, product_slug)
        serializer =  ProductSerializers(instance)
        return Response(serializer.data)

