from django.shortcuts import render

# Create your views here.

# def index(request):
#     return render(request, "products/index.html")

from django.shortcuts import render

def index(request):
    return render(request, 'products/index.html')