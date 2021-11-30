from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/', views.producto, name='producto'),
    path('producto/create', views.productoCreate, name='productoCreate'),
    path('producto/<id>', views.productoDetails, name="productoDetails"),
    path('producto/<id>/update', views.productoUpdate, name="productoUpdate"),
    path('producto/<id>/delete', views.productoDelete, name="productoDelete"),
    path('marca/create', views.marcaCreate, name='marcaCreate'),
    path('marca/<id>', views.marcaDetails, name="marcaDetails"),
    path('marca/<id>/update', views.marcaUpdate, name="marcaUpdate"),
    path('marca/<id>/delete', views.marcaDelete, name="marcaDelete"),
    path('presentacion/create', views.presentacionCreate, name='presentacionCreate'),
    path('presentacion/<id>', views.presentacionDetails, name="presentacionDetails"),
    path('presentacion/<id>/update', views.presentacionUpdate, name="presentacionUpdate"),
    path('presentacion/<id>/delete', views.presentacionDelete, name="presentacionDelete"),
]
