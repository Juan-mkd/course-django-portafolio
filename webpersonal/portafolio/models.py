from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 200),
    description= models.TextField(),
    image= models.ImageField(max_length = 200),
    created=models.DateTimeField(auto_now_add=True),
    update = models.DateTimeField(auto_now=True)