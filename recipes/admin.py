from django.contrib import admin

# Register your models here.

from .models import *

# Inline admin for IngredientList (to manage ingredients inside Recipe)
class IngredientListInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = IngredientList
    extra = 0  # Show empty fields to add more ingredients

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    inlines = [IngredientListInline]


admin.site.register(Ingredient)
admin.site.register(IngredientList)
admin.site.register(MeasurementUnit)