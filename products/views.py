from django.shortcuts import render, HttpResponseRedirect, redirect
from products.models import Game, GameCategory, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Главная страница (приветственная)
def index(request):
    context = {
        "title": "Game Store"
    }
    return render(request, 'products/index.html', context)

# Каталог игр (с фильтром)
def catalog(request, category_id=None, page_number=1):
    context = {
        "title": "Catalog | Game Store",
        "categories": GameCategory.objects.all(),

    }
    if request.user.is_authenticated:
        context.update({
            "basket": [basket.product for basket in Basket.objects.filter(user=request.user)],
            "library": [library.game for library in Library.objects.filter(user=request.user)],
        })

    if category_id:
        filtered_products = Game.objects.filter(category_id=category_id)
    else:
        filtered_products = Game.objects.all()

    pagination = Paginator(filtered_products, 4)
    context.update({
        "products": pagination.page(page_number),
    })

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
    total_sum = sum(bask.product.price * bask.quantity for bask in baskets)

    context = {
        "title": "Basket | Game Store",
        "baskets": baskets,
        "total_quantity": total_quantity,
        "total_sum": total_sum
    }
    return render(request, "products/basket.html", context)


@login_required
def basket_add(request, product_id):
    game = Game.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=game)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=game, quantity=1)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))




def game_detail(request, game_id):
    """Страница одной игры."""
    game = Game.objects.get(id=game_id)

    if request.user.is_authenticated:
        basket = [b.product for b in Basket.objects.filter(user=request.user)]
    else:
        basket = []

    context = {
        "game": game,
        "basket": basket,
        "title": f"{game.name} | Game Store",
        "category_id": game.category_id
    }
    return render(request, "products/game_detail.html", context)

from .models import Library


@login_required
def buy_games(request):
    """Оформить заказ — переносим корзину в библиотеку"""
    baskets = Basket.objects.filter(user=request.user)

    for item in baskets:
        # Добавляем в библиотеку, если ещё нет
        Library.objects.get_or_create(
            user=request.user,
            game=item.product
        )

    # Очищаем корзину
    baskets.delete()

    return redirect('products:library')


@login_required
def library(request):
    """Страница библиотеки пользователя"""
    games = Library.objects.filter(user=request.user)

    context = {
        "title": "Library | Game Store",
        "games": games,
    }
    return render(request, 'products/library.html', context)



