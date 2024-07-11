from django.db import models

# Create your models here.
class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('income', 'Ingreso'),
        ('spend', 'Gasto'),
    ]
    type = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type} - {self.quantity} el {self.date}"