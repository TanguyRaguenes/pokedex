from django.db import models

# Create your models here.
class PokemonModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    def __str__(self):
        return self.name