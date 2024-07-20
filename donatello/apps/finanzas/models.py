from django.db import models
from django.contrib.auth.models import User


class Finanza(models.Model):
    TIPO_CHOICES = [
        ('income', 'Ingreso'),
        ('spend', 'Gasto'),
    ]
    id_finanza = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Finanza #{self.id_finanza}: {self.tipo} - ${self.monto}"