from django.views.generic import ListView

from meals.models import Meal


class MealListView(ListView):
    model = Meal
