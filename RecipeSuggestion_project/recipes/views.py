from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecipeSerializer
from .models import Ingredient, Category, Recipe
from .forms import RecipeForm
from .utils import filter_recipes_by_criteria
import logging
logger = logging.getLogger('django')

class AddRecipeView(APIView):
    template_name = 'add_recipe.html'

    def get(self, request, *args, **kwargs):
        ingredients = Ingredient.objects.all()
        categories = Category.objects.all()
        return render(request, self.template_name, {
            "ingredients": ingredients,
            "categories": categories,
            "name": "Add Recipe"
        })

    def post(self, request, *args, **kwargs):
        try:
            serializer = RecipeSerializer(data=request.data)
            if serializer.is_valid():
                recipe = serializer.save()  # データベースに保存
                return Response({"message": "レシピが正常に追加されました！", "recipe_id": recipe.id}, status=status.HTTP_201_CREATED)
            else:
                logger.debug(f"Validation errors: {serializer.errors}")
                return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error while adding recipe: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RecipeListView(APIView):
    template_name = 'recipes_list.html'

    def get(self, request, *args, **kwargs):
        try:
            recipes = Recipe.objects.all()
            return render(request, self.template_name, {
                "recipes": recipes,
                "name": "Recipe List"
            })
        except Exception as e:
            logger.error(f"Error while fetching recipes: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RecipeDetailView(APIView):
    template_name = 'recipe_detail.html'

    def get(self, request, recipe_id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = RecipeForm(instance=recipe)
        return render(request, self.template_name, {
            "recipe": recipe,
            "form": form,
        })

    def post(self, request, recipe_id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"success": True})
            return redirect('recipe_detail', recipe_id=recipe.id)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
        return render(request, self.template_name, {
            "recipe": recipe,
            "form": form
        })

    def delete(self, request, recipe_id, *args, **kwargs):
        try:
            recipe = get_object_or_404(Recipe, id=recipe_id)
            recipe.delete()
            return JsonResponse({"message": "レシピが正常に削除されました。"}, status=200)
        except Exception as e:
            logger.error(f"Error while deleting recipe: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

class RecipeSuggestionView(APIView):
    template_name = 'recipe_suggestion.html'

    def get(self, request, *args, **kwargs):
        ingredients = Ingredient.objects.all()
        categories = Category.objects.all()
        return render(request, self.template_name, {
            "ingredients": ingredients,
            "categories": categories,
            "name": "Recipe Suggestion",
            "recipes": None,  # 初期値として None を渡す
            "error": None  # 初期値として None を渡す
        })

    def post(self, request, *args, **kwargs):
        try:
            logger.debug(f"POST data received: {request.POST}")
            logger.debug(f"Ingredients received: {request.POST.getlist('ingredients')}")
            selected_ingredients = request.data.getlist('ingredients', [])

            # Check if at least one ingredient is selected
            if not selected_ingredients:
                return render(request, self.template_name, {
                    "error": "少なくとも1つの食材を選択してください。",
                    "ingredients": Ingredient.objects.all(),
                    "categories": Category.objects.all(),
                    "name": "Recipe Suggestion",
                    "recipes": None  # レシピがない場合もテンプレートで処理できるようにする
                })

            selected_category = request.data.get('category', None)

            # Utility function to filter recipes
            recipes = filter_recipes_by_criteria(selected_ingredients, selected_category)

            return render(request, self.template_name, {
                "recipes": recipes,
                "ingredients": Ingredient.objects.all(),
                "categories": Category.objects.all(),
                "selected_ingredient_ids": selected_ingredients,
                "selected_category_id": selected_category,
                "name": "Recipe Suggestion"
            })
        except Exception as e:
            logger.error(f"Error while suggesting recipes: {str(e)}")
            return render(request, self.template_name, {
                "error": f"エラーが発生しました: {str(e)}",
                "ingredients": Ingredient.objects.all(),
                "categories": Category.objects.all(),
                "name": "Recipe Suggestion",
                "recipes": None
            })