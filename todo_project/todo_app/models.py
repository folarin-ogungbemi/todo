from django.db import models

# Create your models here.


class Todo(models.Model):

    name = models.CharField(max_length=50, null=True, blank=True)
    done = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.name
