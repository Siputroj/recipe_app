from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    ingredient = models.CharField(max_length=75)

    def __str__(self):
        return str(self.ingredient)


class MeasurementUnit(models.Model):
    id = models.AutoField(primary_key=True)
    unit = models.CharField(max_length=75)

    def __str__(self):
        return str(self.unit)

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='IngredientList')
    instruction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.title)


class IngredientList(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    measurement = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return f"{self.measurement} {self.unit} of {self.ingredient}"
