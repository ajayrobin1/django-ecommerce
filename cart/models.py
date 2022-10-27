from django.db import models

from django.contrib.auth.models import User

from products.models import Product

# Create your models here.
class Cart(models.Model):
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='added_by'
    )
    added_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='added_product'
    )

    def __str__(self):
        return f"{self.added_by.id} added {self.added_product.id}"

    class Meta:
        unique_together = ('added_by', 'added_product',)