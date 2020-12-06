from django.contrib import admin

from meals.models import Ingredient, IngredientQuantity, Meal


class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity
    extra = 3


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = ("name",)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    fields = ("name", "description", "season", "url", "difficulty")
    list_display = ("name", "description", "season", "url", "difficulty")
    list_filter = ("season", "difficulty")
    inlines = (IngredientQuantityInline,)
