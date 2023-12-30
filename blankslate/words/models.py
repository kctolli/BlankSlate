from django.db import models

from lib.date import Date

# Create your models here.
class Word(models.Model):
    class Fix(models.TextChoices):
        suffix = "suffix"
        prefix = "prefix"
    
    word = models.CharField(
        max_length = 255,
        null=False
    )

    fix = models.CharField(
        max_length = 6,
        choices = Fix,
        default = Fix.prefix,
        null=False
    )

    def getMaxId(self):
        return self.objects.all().count()
