from django import template
from news.models import Category



register = template.Library()

@register.simple_tag(name = 'get_list_categories')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('list_categories.html')
def show_categories(argl1='Hello', argl2='world'):
    categories = Category.objects.all()
    return {"categories":categories, "argl1" : argl1, "argl2" : argl2}