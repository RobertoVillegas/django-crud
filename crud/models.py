from django.db import models

# Create your models here.


class Marca(models.Model):
    marca_nombre = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.marca_nombre


class Presentacion(models.Model):
    presentacion_nombre = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.presentacion_nombre


class Producto(models.Model):
    producto_precio = models.FloatField(default=1)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
