from django.contrib import admin
from .models import Ingredient

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'reading', 'type')
    search_fields = ('name', 'reading')
    list_filter = ('type',)

admin.site.register(Ingredient, IngredientAdmin)
