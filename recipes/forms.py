from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, IngredientList

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instruction']

class IngredientListForm(forms.ModelForm):
    class Meta:
        model = IngredientList
        fields = ['ingredient', 'measurement', 'unit']

"""
inlineformset allows us to have a form inside of another form.
extra = 1 adds an empty line in the form for us to fill in the data, this is optional
"""
IngredientListFormSet = inlineformset_factory(Recipe, IngredientList, form = IngredientListForm, extra = 1)
