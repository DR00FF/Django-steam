from django.urls import path
from products.views import catalog
from products.views import basket, basket_add, basket_delete, game_detail, buy_games, library

app_name = 'products'

urlpatterns = [
    path('', catalog, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('page/<int:page_number>', catalog, name="page_number"),
    path('<int:category_id>',catalog, name="category"),
    path('basket', basket, name='basket'),
    path('game/<int:game_id>/', game_detail, name='game_detail'),
    path('basket-add/<int:product_id>', basket_add, name="basket_add"),
    path('basket-delete/<int:basket_id>', basket_delete, name="basket_delete"),
    path('category/<int:category_id>/page/<int:page_number>/', catalog, name="category_page"),
    path('buy/', buy_games, name='buy_games'),
    path('library/', library, name='library'),

]



