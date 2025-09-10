from django.db import models

# Create your models here.
class PokemonModel(models.Model):
    id = models.IntegerField(primary_key=True)
    original_name = models.CharField(max_length=100)
    french_name = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.original_name