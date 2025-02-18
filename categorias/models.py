from django.db import models

# Create your models here.

class Categoria(models.Model):
    # aqui va los atributos de la clase
    nombre = models.CharField(max_length=100)
    #los campos urlsfields limitan los caracteres a 200 por defecto
    imagen = models .URLField()
    
    def __str__(self):
        return self.nombre