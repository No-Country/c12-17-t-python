from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField('Nombre del producto', max_length=100)
    price =  models.DecimalField('Precio', max_digits=6, decimal_places=2)
    description = models.TextField('Descripción', blank=True)
    category = models.CharField('Categoria', max_length=120)
    image = models.ImageField('Imagen')

    def __str__(self):
        return str(self.id)

