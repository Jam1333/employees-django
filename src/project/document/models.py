from django.db import models
from django.utils import timezone
from employee.models import Employee

class Document(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField()
    employees = models.ManyToManyField(Employee, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
