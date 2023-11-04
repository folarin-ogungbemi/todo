from django.db import models
from django.utils import timezone

# Create your models here.


class Todo(models.Model):

    name = models.CharField(max_length=50, null=True, blank=True)
    content = models.CharField(max_length=225, null=True, blank=True)
    done = models.BooleanField(null=True, blank=True, default=False)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
