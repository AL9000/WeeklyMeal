import django_filters
from django import forms

from meals.models import Meal


class MealFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nom de recette",
        })
    )

    class Meta:
        model = Meal
        fields = ["name", ]
