from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    cpf = models.IntegerField()

    def __str__(self):
        return self.name
