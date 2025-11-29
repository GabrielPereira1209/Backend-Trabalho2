from django.db import models
from django.conf import settings

class Spot(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=(('covered','Covered'),('uncovered','Uncovered'),('garage','Garage')))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='spots')

    def __str__(self):
        return self.title
