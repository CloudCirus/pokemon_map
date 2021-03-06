from django.db import models
from django.db.models.deletion import CASCADE 


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Имя', max_length=200)
    image = models.ImageField(verbose_name='Изображение', null=True)

    def __str__(self) -> str:
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=CASCADE, null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=None)
    disappeared_at = models.DateTimeField(default=None)
    level = models.IntegerField(default=None)
    health = models.IntegerField(default=None)
    strength = models.IntegerField(default=None)
    defence = models.IntegerField(default=None)
    stamina = models.IntegerField(default=None)

    def __str__(self) -> str:
        return f'{self.pokemon} {self.lat}/{self.lon}'
