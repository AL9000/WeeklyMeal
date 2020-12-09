from django.urls import path
from django_filters.views import FilterView

from meals.filters import MealFilter
from meals.views import MealDetailView, CartView


app_name = "meals"
urlpatterns = [
    path("", FilterView.as_view(filterset_class=MealFilter), name="meal-list"),
    path("<int:pk>/", MealDetailView.as_view(), name="meal-detail"),
    path("cart/", CartView.as_view(), name="cart"),
]
