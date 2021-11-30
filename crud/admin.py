from django.contrib import admin
from .models import Marca, Presentacion, Producto

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto_precio', 'marca', 'presentacion')
    ordering = ['id']


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca_nombre', 'created_on')
    ordering = ['id']


class PresentacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'presentacion_nombre', 'created_on')
    ordering = ['id']


# Register your models here.
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Presentacion, PresentacionAdmin)
admin.site.register(Producto, ProductoAdmin)
