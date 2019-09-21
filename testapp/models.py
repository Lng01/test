from django.db import models

# Create your models here.
from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=128)
    content = models.CharField(max_length=128)
