from django.urls import path
from .views import (
    html_crud_view,
    delete_product_view,
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    edit_product_view,  # Importar la vista de edición
)

urlpatterns = [
    path('', html_crud_view, name='html_crud_view'),  # Ruta para la vista HTML con CRUD
    path('delete/<int:product_id>/', delete_product_view, name='delete_product'),  # Ruta para eliminar productos
    path('edit/<int:product_id>/', edit_product_view, name='edit_product'),  # Nueva ruta para editar
    path('api/products/', ProductListCreateAPIView.as_view(), name='product_list_create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_detail'),
]
