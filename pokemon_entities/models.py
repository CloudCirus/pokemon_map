from django.db import models 


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Имя', max_length=200)
    image = models.ImageField(verbose_name='Изображение', null=True)

    def __str__(self) -> str:
        return f'{self.title}'
