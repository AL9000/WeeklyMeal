from django.urls import path

from meals.views import MealListView

urlpatterns = [
    path('', MealListView.as_view(), name="meal-list"),
]
