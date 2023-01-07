from django.shortcuts import render, get_object_or_404
from .models import Recipe, Tag, RecipeIngredient
# Create your views here.

def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-id')
    ctx = {
        'recipes': recipes
    }
    return  render(request, 'recipe/list.html', ctx)



def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    ctx = {
        'recipe': recipe
    }
    return render(request, 'recipe/detail.html', ctx)


def recipe_create(request):
    pass