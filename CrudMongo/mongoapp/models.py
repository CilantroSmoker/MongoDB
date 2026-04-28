from djongo import models

STATUS_CHOICES = [
    ('disponible', 'Disponible'),
    ('vendido', 'Vendido'),
    ('reservado', 'Reservado'),
]

class Vehiculo(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponible')

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    class Meta:
        collection = 'vehiculos'