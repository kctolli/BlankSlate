from django.db import models

# Create your models here.
class Word(models.Model):
    class Fix(models.TextChoices):
        suffix = "suffix"
        prefix = "prefix"
    
    word = models.CharField(max_length=255)

    response = models.CharField(
        max_length=6,
        choices=Fix,
        default=Fix.suffix,
    )

