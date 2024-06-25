from django.db import models

# Create your models here.
class Pizza(models.Model):
    nombre_pizza = models.CharField(max_length= 20, unique=True, null=False)
    precio= models.IntegerField(null=False)

    def __str__(self) -> str:
        return f"{self.nombre_pizza}, {self.precio}"