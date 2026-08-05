from django.db import models

# Create your models here.
class GameCategory(models.Model):
     name = models.CharField(max_length=32, unique=True)
     description = models.TextField(blank=True)

     def __str__(self):
         return self.name

class Game(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to="products_media", blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=128, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    genre = models.CharField(max_length=32, blank=True)
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.category.name}"