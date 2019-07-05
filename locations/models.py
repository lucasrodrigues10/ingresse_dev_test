from django.db import models


class Location(models.Model):
    street = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.street
