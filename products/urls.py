from django.urls import path
from products.views import catalog
from products.views import basket, basket_add, basket_delete, game_detail

app_name = 'products'

urlpatterns = [
    path('', catalog, name='home'),
    path('basket', basket, name='basket'),
    path('game/<int:game_id>/', game_detail, name='game_detail'),
    path('basket-add/<int:product_id>', basket_add, name="basket_add"),
    path('basket-delete/<int:basket_id>', basket_delete, name="basket_delete"),

]