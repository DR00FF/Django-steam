from django.shortcuts import render, HttpResponseRedirect
from products.models import Game, GameCategory, Basket
from django.contrib.auth.decorators import login_required

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

@login_required
def basket(request):
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = sum(bask.quantity for bask in baskets)
    total_sum = sum(bask.product.price for bask in baskets)

    context = {
        "baskets": baskets,
        "total_quantity": total_quantity,
        "total_sum": total_sum
    }
    return render(request, "products/basket.html", context)
@login_required
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
@login_required
def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))