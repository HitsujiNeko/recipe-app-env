from django.urls import path
from .views import AddRecipeView, RecipeListView, RecipeDetailView, RecipeSuggestionView

urlpatterns = [
    path('add-recipe/', AddRecipeView.as_view(), name='add_recipe'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:recipe_id>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe-suggestion/', RecipeSuggestionView.as_view(), name='recipe_suggestion'),
]