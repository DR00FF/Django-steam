from django.contrib import admin

# Register your models here.

from products.models import Game, GameCategory

admin.site.register(Game)
admin.site.register(GameCategory)