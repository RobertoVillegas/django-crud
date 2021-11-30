from .models import Marca, Presentacion, Producto
from django import forms


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'


class PresentacionForm(forms.ModelForm):
    class Meta:
        model = Presentacion
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
