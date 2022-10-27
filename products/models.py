from django.db import models

from sorl.thumbnail import ImageField

from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    image = ImageField()
    discription= models.TextField()
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name