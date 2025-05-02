from django.db import models
from django.contrib.auth.models import User

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_comida = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    dia = models.DateField()
    hora = models.TimeField()
    personas = models.IntegerField()

def __str__(self):
#        return f"Reserva en {self.restaurante.nombre} para el {self.dia} a las {self.hora} para {self.personas} personas"
        return f"{self.usuario.username} - reservó en {self.restaurante} - el día {self.dia} a las {self.hora} para {self.personas} personas"
