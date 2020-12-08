from django.views.generic import DetailView

from meals.models import Meal


class MealDetailView(DetailView):
    model = Meal
