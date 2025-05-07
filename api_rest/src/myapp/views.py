from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# Vista para manejar el CRUD en el HTML
def html_crud_view(request):
    if request.method == "POST":
        # Crear o actualizar un producto
        product_id = request.POST.get("id")
        name = request.POST.get("name")
        price = request.POST.get("price")
        stock = request.POST.get("stock")

        if product_id:  # Actualizar producto existente
            product = get_object_or_404(Product, id=product_id)
            product.name = name
            product.price = price
            product.stock = stock
            product.save()
        else:  # Crear un nuevo producto
            Product.objects.create(name=name, price=price, stock=stock)

        return redirect("html_crud_view")

    elif request.method == "GET":
        # Obtener todos los productos para mostrarlos en la tabla
        products = Product.objects.all()
        return render(request, 'myapp/index.html', {"products": products})

# Vista para eliminar un producto
def delete_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect("html_crud_view")

# Vista para devolver JSON con datos del almacén
class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# Vista para listar y crear productos (API REST)
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Vista para recuperar, actualizar y eliminar productos (API REST)
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def root_view(request):
    return JsonResponse({"message": "Bienvenido a la API REST"})  # Vista para la URL raíz

def edit_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")
        product.save()
        return redirect("html_crud_view")
    return render(request, 'myapp/editar.html', {"product": product})
