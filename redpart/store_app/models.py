from django.db import models

# Create your models here.


class Shoe(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='shoes')

    def __str__(self):
        return self.name