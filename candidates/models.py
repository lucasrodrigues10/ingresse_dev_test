from django.db import models

from companies.models import Company
from feedbacks.models import Feedback
from locations.models import Location


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    cpf = models.IntegerField()
    companies = models.ManyToManyField(Company)
    feedback = models.ManyToManyField(Feedback)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
