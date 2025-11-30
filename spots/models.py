# importa módulos necessários para models
from django.db import models
from django.conf import settings

 # modelo de vaga
class Spot(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=(('covered','Covered'),('uncovered','Uncovered'),('garage','Garage')))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='spots')


    # retorna representação em string da vaga
    def __str__(self):
        return self.title
