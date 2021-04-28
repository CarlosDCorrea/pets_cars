from django.db import models

# Create your models here.
class Tipos(models.Model):
    codigo=models.IntegerField(null=False)
    nombre=models.CharField(max_length=150, null=False)
    abreviatura=models.CharField(max_length=150, null=False)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Razas(models.Model):
    codigo=models.IntegerField(null=False)
    nombre=models.CharField(max_length=150, null=False)
    abreviatura=models.CharField(max_length=150, null=False)
    id_tipo=models.ForeignKey(Tipos, on_delete=models.CASCADE)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Mascotas(models.Model):
    codigo=models.IntegerField(null=False)
    id_tipo=models.ForeignKey(Tipos, on_delete=models.CASCADE)
    id_raza=models.ForeignKey(Razas, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=150, null=False)
    tiene_vacunas=models.BooleanField(null=True)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()