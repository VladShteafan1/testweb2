from django.db.models import Count
from django.shortcuts import render
from .models import Recipe, Category

def main(request):
    latest_recipes = Recipe.objects.order_by('-created_at')[:5]
    return render(request, 'main.html', {'latest_recipes': latest_recipes})

def category_list(request):
    categories = Category.objects.annotate(num_recipes=Count('recipe'))
    return render(request, 'category_list.html', {'categories': categories})
