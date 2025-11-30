
# importa módulos necessários para models
from django.db import models
from django.conf import settings
from spots.models import Spot

 # modelo de aluguel de vaga
class Rental(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='rentals')
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rentals')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=(('active','Active'),('pending','Pending'),('cancelled','Cancelled')), default='pending')
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2)


    # retorna representação em string do aluguel
    def __str__(self):
        return f"{self.spot} - {self.tenant}"
