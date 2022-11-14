from tkinter import CASCADE
from django.db import models

from sorl.thumbnail import ImageField

from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    date = models.DateTimeField(auto_now=True)
    image = ImageField()
    discription= RichTextUploadingField()
    rating=models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        null=True
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name