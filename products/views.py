from django.shortcuts import render, HttpResponseRedirect
from products.models import Game, GameCategory, Basket

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

def basket(request):
    context = {
        "basket": Basket.objects.filter(user=request.user)
    }
    return render(request, "products/basket.html", context)

def basket_add(request, product_id):
    game = Game.object.get(id=product_id)
    baskets = Basket.object.filter(user=request.user, product=game)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=game, quantity=1)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        basket = baskets.first()
        basket.quantity +=1
        basket.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))