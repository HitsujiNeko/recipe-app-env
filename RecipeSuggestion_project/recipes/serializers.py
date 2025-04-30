from rest_framework import serializers
from .models import Recipe, Category
from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer
from .utils import extract_youtube_thumbnail

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ingredient.objects.all(), help_text="使用する食材を選択してください"
    )
    thumbnail = serializers.CharField(required=False, allow_blank=True, help_text="サムネイル画像のURLを入力してください。空の場合は自動生成されます。")

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'url', 'thumbnail', 'notes', 'ingredients', 'categories', 'created_at', 'updated_at']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        categories_data = validated_data.pop('categories')

        # URLからサムネイル画像を自動抽出する機能
        youtube_url = validated_data.get('url')
        if youtube_url and not validated_data.get('thumbnail'):
            validated_data['thumbnail'] = extract_youtube_thumbnail(youtube_url)

        recipe = Recipe.objects.create(**validated_data)
        recipe.ingredients.set(ingredients_data)
        recipe.categories.set(categories_data)
        return recipe