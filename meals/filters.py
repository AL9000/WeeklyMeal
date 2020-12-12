import django_filters
from django import forms
from django.forms import CheckboxSelectMultiple

from meals.models import Meal, Season


class MealFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nom de recette",
        })
    )
    seasons = django_filters.ModelMultipleChoiceFilter(
        queryset=Season.objects.all(),
        widget=CheckboxSelectMultiple(attrs={
            "class": "list-group list-group-horizontal"
        }),
    )

    class Meta:
        model = Meal
        fields = ["name", "seasons"]
