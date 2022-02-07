from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image


class Worker(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
    image = models.ImageField(upload_to ='uploads/', null=True, blank=True)


    class Meta:
        ordering = ['surname']

    def __str__(self):
        return self.name


