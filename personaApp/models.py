from django.db import models

# Create your models here.


class persona(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    nac= models.CharField(max_length=50)
    dui= models.CharField(max_length=100)
    telefono= models.CharField(max_length=20)
    direccion= models.CharField(max_length=100)

    def getNombre(self):
        return self.nombre