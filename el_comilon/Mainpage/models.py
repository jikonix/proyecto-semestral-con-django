from django.db import models
from Adminpage.models import Comidas
# Modelos.


class Carro(models.Model):
    key_sesion= models.CharField(max_length=40, null=True, blank=True)
    fecha_creacion= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Carrito N°: {self.id}'


class items_carro(models.Model):
    carro= models.ForeignKey(Carro, on_delete=models.CASCADE, related_name="items")
    comida= models.ForeignKey(Comidas, on_delete=models.CASCADE)
    cantidad= models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.cantidad} - {self.comida.item}'

    def obtener_precio(self):
        return self.cantidad * self.comida.precio