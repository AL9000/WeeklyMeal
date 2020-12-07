from django.urls import path
from django_filters.views import FilterView

from meals.filters import MealFilter

urlpatterns = [
    path('', FilterView.as_view(filterset_class=MealFilter)),
]
