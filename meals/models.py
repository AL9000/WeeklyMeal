from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ingredient(TimeStampMixin):
    name = models.CharField("Nom", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ingrédient"


class Season(models.Model):
    class Seasons(models.TextChoices):
        spring = "SP", "Printemps"
        summer = "SU", "Été"
        autumn = "AU", "Automne"
        winter = "WI", "Hiver"

    name = models.CharField("Nom", choices=Seasons.choices, max_length=50)

    def __str__(self):
        return self.get_name_display()


class Meal(TimeStampMixin):
    class CompletionTimes(models.TextChoices):
        fast = "FT", "Rapide"
        medium = "MD", "Moyen"
        long = "LG", "Long"

    class Difficulties(models.IntegerChoices):
        easy = 1, "Facile"
        normal = 2, "Normal"
        hard = 3, "Difficile"
        expert = 4, "Expert"

    name = models.CharField("Nom", max_length=50)
    comment = models.TextField("Commentaire", max_length=500, blank=True)
    seasons = models.ManyToManyField(Season, verbose_name="Saisons", blank=True)
    url = models.URLField("url de la recette", blank=True)
    picture_url = models.URLField("url de l'image", blank=True)
    ingredients = models.ManyToManyField(Ingredient, through="IngredientQuantity")
    difficulty = models.IntegerField("Difficulté", choices=Difficulties.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Repas"
        verbose_name_plural = "Repas"


class IngredientQuantity(TimeStampMixin):
    class Units(models.TextChoices):
        grams = "GR", "Grammes"
        centiliter = "CL", "Centilitre"
        unit = "UN", "Unité"
        pinch = "PI", "Pincée"
        slice = "SL", "Tranche"

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.FloatField("Quantité")
    unit = models.CharField("Unité", choices=Units.choices, max_length=50)

    def __str__(self):
        return f"{self.ingredient} pour {self.meal} [{self.quantity} {self.get_unit_display()}]"

    class Meta:
        verbose_name = "Ingrédient"
