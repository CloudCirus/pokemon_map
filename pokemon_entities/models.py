from django.db import models 


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Имя', max_length=200)
