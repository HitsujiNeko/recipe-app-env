from django.db import models
from ingredients.models import Ingredient

class Category(models.Model):
    name = models.CharField(max_length=50)  # カテゴリ名

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="レシピ名を入力してください") 
    url = models.URLField(unique=True, help_text="YouTubeのURLを入力してください")  
    thumbnail = models.URLField(blank=True, null=True, help_text="画像URLを入力してください（入力無しの場合、サムネイル画像")
    notes = models.TextField(blank=True, null=True, help_text="備考を入力してください") 
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes', help_text="使用する食材を選択してください")  
    categories = models.ManyToManyField(Category, related_name='recipes', help_text="カテゴリを選択してください") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
