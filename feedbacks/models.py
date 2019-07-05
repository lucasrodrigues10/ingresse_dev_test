from django.contrib.auth.models import User
from django.db import models


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
