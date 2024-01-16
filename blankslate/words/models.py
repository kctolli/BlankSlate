from django.db import models

from lib.randomint import randomint

# Create your models here.
class Word(models.Model):
    class Fix(models.TextChoices):
        prefix = "prefix"
        suffix = "suffix"
    
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

    def getAllWords():
        """
        Get all the words from the objects in the database.

        Parameters:
            self (object): The instance of the class.
        
        Returns:
            object: All the words from the database.
        """
        return Word.objects.all()

    def getMaxId():
        """
        Get the maximum ID value from the objects.

        Returns:
            int: The maximum ID value.
        """
        return Word.objects.all().count()
    
    def getRandomWord():
        """
        Get a random word from the objects in the database.

        Parameters:
            self (object): The instance of the class.
        
        Returns:
            object: A randomly selected word from the database.
        """
        id = randomint(Word.getMaxId())
        return Word.objects.get(id=id)
