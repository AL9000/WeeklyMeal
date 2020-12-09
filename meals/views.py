from django.db.models import Prefetch
from django.views.generic import DetailView, ListView

from meals.models import IngredientQuantity, Meal


class MealDetailView(DetailView):
    model = Meal


class CartView(ListView):
    model = Meal
    template_name = "meals/cart.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        meals = self.request.GET.getlist("meal")
        queryset = queryset.filter(pk__in=meals).prefetch_related(
            Prefetch(
                "ingredientquantity_set",
                queryset=IngredientQuantity.objects.distinct(),
                to_attr="cart_ingredients",
            ),
        )
        return queryset
