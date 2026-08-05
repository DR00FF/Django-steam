from django.shortcuts import render
from products.models import Game, GameCategory
# Главная страница (приветственная)
def index(request):
    context = {
        "title": "Game Store"
    }
    return render(request, 'products/index.html', context)

# Каталог игр (с фильтром)
def catalog(request):
    context = {
        "title": "Catalog | Game Store",
        "products": Game.objects.all() ,
        "categories": GameCategory.objects.all(),
    }
    return render(request, 'products/catalog.html', context)

def about(request):
    context = {
        "title": "About us | Game Store",
    }
    return render(request, 'products/about_us.html', context)