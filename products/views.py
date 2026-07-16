from django.shortcuts import render

# Главная страница (приветственная)
def index(request):
    return render(request, 'products/index.html')

# Каталог игр (с фильтром)
def catalog(request):
    return render(request, 'products/catalog.html')