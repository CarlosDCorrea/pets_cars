from django.db import models

# Create your models here.

class Paises(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=150, null=False)
    abreviatura=models.CharField(max_length=150, null=False)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Ciudades(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=150, null=False)
    abreviatura=models.CharField(max_length=150, null=False)
    id_pais=models.ForeignKey(Paises, on_delete=models.CASCADE)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Afiliados(models.Model):
    nombres=models.CharField(max_length=150, null=False)
    apellidos=models.CharField(max_length=150, null=False)
    numero_movil=models.IntegerField()
    direccion=models.CharField(max_length=150, null=False)
    email=models.EmailField()
    id_ciudad=models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()