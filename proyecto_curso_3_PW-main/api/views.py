from rest_framework import viewsets
from rest_framework.response import Response
from .models import Producto
from .serial import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('-fecha_creacion')  
    serializer_class = ProductoSerializer  
