from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Category 1")
        self.category2 = Category.objects.create(name="Category 2")
        self.recipe1 = Recipe.objects.create(name="Recipe 1", category=self.category1)
        self.recipe2 = Recipe.objects.create(name="Recipe 2", category=self.category1)
        self.recipe3 = Recipe.objects.create(name="Recipe 3", category=self.category2)
        self.recipe4 = Recipe.objects.create(name="Recipe 4", category=self.category2)
        self.recipe5 = Recipe.objects.create(name="Recipe 5", category=self.category1)
        self.recipe6 = Recipe.objects.create(name="Recipe 6", category=self.category2)

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/main.html')
        self.assertEqual(len(response.context['latest_recipes']), 5)
        self.assertQuerysetEqual(
            response.context['latest_recipes'],
            [self.recipe6, self.recipe5, self.recipe4, self.recipe3, self.recipe2],
            transform=lambda x: x
        )

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/category_list.html')
        self.assertEqual(len(response.context['categories']), 2)
        categories = response.context['categories']
        self.assertEqual(categories[0].num_recipes, 3)
        self.assertEqual(categories[1].num_recipes, 3)

