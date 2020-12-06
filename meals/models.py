from django.db import models


class Ingredient(models.Model):
    name = models.CharField("Nom", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ingrédient"


class Meal(models.Model):
    class CompletionTimes(models.TextChoices):
        fast = "FT", "Rapide"
        medium = "MD", "Moyen"
        long = "LG", "Long"

    class Difficulties(models.IntegerChoices):
        easy = 1, "Facile"
        normal = 2, "Normal"
        hard = 3, "Difficile"
        expert = 4, "Expert"

    class Seasons(models.TextChoices):
        spring = "SP", "Printemps"
        summer = "SU", "Été"
        autumn = "AU", "Automne"
        winter = "WI", "Hiver"

    name = models.CharField("Nom", max_length=50)
    description = models.TextField("Description", max_length=500, blank=True)
    season = models.CharField("Saison", choices=Seasons.choices, max_length=50, blank=True)
    url = models.URLField("url", blank=True)
    ingredients = models.ManyToManyField(Ingredient, through="IngredientQuantity")
    difficulty = models.IntegerField("Difficulté", choices=Difficulties.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Repas"
        verbose_name_plural = "Repas"


class IngredientQuantity(models.Model):
    class Units(models.TextChoices):
        grams = "GR", "Grammes"
        centiliter = "CL", "Centilitre"
        unit = "UN", "Unité"
        pinch = "PI", "Pincée"

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.FloatField("Quantité")
    unit = models.CharField("Unité", choices=Units.choices, max_length=50)

    def __str__(self):
        return f"{self.ingredient} pour {self.meal} [{self.quantity} {self.get_unit_display()}]"

    class Meta:
        verbose_name = "Ingrédient"
