from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),          # Главная страница
    path('catalog/', views.catalog, name='catalog'),  # Каталог игр
]