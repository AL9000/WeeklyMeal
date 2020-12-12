import django_filters
from django import forms
from django.db.models import Q
from django.forms import CheckboxSelectMultiple

from meals.models import Meal, Season


class MealFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="meal_filter",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nom de recette, commentaire, ingrédient",
        })
    )
    seasons = django_filters.ModelMultipleChoiceFilter(
        queryset=Season.objects.all(),
        widget=CheckboxSelectMultiple(attrs={
            "class": "list-group list-group-horizontal"
        }),
    )
    difficulty = django_filters.ChoiceFilter(
        choices=Meal.Difficulties.choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def meal_filter(self, queryset, name, value):
        return Meal.objects.filter(
            Q(name__icontains=value) |
            Q(comment__icontains=value) |
            Q(ingredients__name__icontains=value)
        ).distinct()

    class Meta:
        model = Meal
        fields = ["search", "seasons", "difficulty"]
