from django.contrib import admin

from meals.models import Ingredient, IngredientQuantity, Meal


admin.site.site_header = "Les menus de la semaine"
admin.site.site_title = "Les menus de la semaine"
admin.site.index_title = "Les menus de la semaine"


class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity
    extra = 3


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = ("name",)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    fields = ("name", "description", "seasons", "url", "difficulty")
    list_display = ("name", "description", "get_seasons", "url", "difficulty")
    list_filter = ("seasons", "difficulty")
    inlines = (IngredientQuantityInline,)

    def get_seasons(self, meal):
        return [season.get_name_display() for season in meal.seasons.all()]

    get_seasons.short_description = "Saisons"
