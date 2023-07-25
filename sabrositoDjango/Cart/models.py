from django.db import models
from django.contrib.auth.models import User
from sabrositoDjango.utils import unique_slug_generator
from django.db.models.signals import pre_save
# Create your models here.

class Product(models.Model):
    name = models.CharField('Nombre del producto', max_length=100)
    price =  models.DecimalField('Precio', max_digits=6, decimal_places=2)
    description = models.TextField('Descripción', blank=True)
    category = models.CharField('Categoria', max_length=120)
    image = models.ImageField('Imagen', blank=True)
    slug = models.SlugField(null=True, blank=True)
# >>>>>>> a5a342e4edf9c9019a189430712b0365661231c7

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Product_Order(models.Model):
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

# >>>>>>> a5a342e4edf9c9019a189430712b0365661231c7


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Product)