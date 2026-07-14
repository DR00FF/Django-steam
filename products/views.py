from django.shortcuts import render

# Наши игры (список)
GAMES = [
    {'id': 1, 'title': 'CyberQuest 2077', 'genre': 'action', 'price': 1299, 'old_price': 2599, 'rating': 9.2, 'discount': 30, 'icon': 'fa-dragon', 'description': 'Футуристический экшен в открытом мире'},
    {'id': 2, 'title': 'Dragon Age: Origins', 'genre': 'rpg', 'price': 1799, 'old_price': 2599, 'rating': 9.5, 'discount': 40, 'icon': 'fa-hat-wizard', 'description': 'Эпическое фэнтези с глубоким сюжетом'},
    {'id': 3, 'title': 'Mystic Legacy', 'genre': 'rpg', 'price': 1499, 'old_price': 2499, 'rating': 8.8, 'discount': 60, 'icon': 'fa-scroll', 'description': 'Магическая RPG с открытым миром'},
    {'id': 4, 'title': 'Mech Warfare', 'genre': 'action', 'price': 999, 'old_price': 2499, 'rating': 9.0, 'discount': 35, 'icon': 'fa-robot', 'description': 'Битвы на гигантских роботах'},
    {'id': 5, 'title': 'Dark Souls III', 'genre': 'action', 'price': 1699, 'old_price': 2599, 'rating': 9.7, 'discount': 25, 'icon': 'fa-skull', 'description': 'Хардкорный дарк-фэнтези экшен'},
    {'id': 6, 'title': 'Star Horizon', 'genre': 'strategy', 'price': 999, 'old_price': 1999, 'rating': 8.5, 'discount': 50, 'icon': 'fa-meteor', 'description': 'Космическая стратегия в реальном времени'},
    {'id': 7, 'title': 'The Witcher 3', 'genre': 'rpg', 'price': 1499, 'old_price': 2999, 'rating': 9.8, 'discount': 50, 'icon': 'fa-wolf', 'description': 'Ведьмак 3: Дикая Охота'},
    {'id': 8, 'title': 'Counter-Strike 2', 'genre': 'shooter', 'price': 0, 'old_price': 0, 'rating': 8.9, 'discount': 0, 'icon': 'fa-crosshairs', 'description': 'Бесплатный шутер от Valve'},
]

GENRES = [
    {'slug': 'all', 'name': 'Все игры'},
    {'slug': 'action', 'name': 'Экшен'},
    {'slug': 'rpg', 'name': 'RPG'},
    {'slug': 'strategy', 'name': 'Стратегии'},
    {'slug': 'shooter', 'name': 'Шутеры'},
]

# Главная страница (приветственная)
def index(request):
    return render(request, 'products/index.html')

# Каталог игр (с фильтром)
def catalog(request):
    genre_slug = request.GET.get('genre', 'all')
    if genre_slug != 'all':
        filtered_games = [g for g in GAMES if g['genre'] == genre_slug]
    else:
        filtered_games = GAMES
    context = {
        'games': filtered_games,
        'genres': GENRES,
        'current_genre': genre_slug,
    }
    return render(request, 'products/catalog.html', context)