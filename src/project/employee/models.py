from django.db import models
from django.utils import timezone

from position.models import Position

class Employee(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="employees"
    )

    def __str__(self):
        return self.name
