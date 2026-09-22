from django.contrib import admin
# Register your models here.

from products.models import Game, GameCategory, Basket, Library


admin.site.register(GameCategory)
admin.site.register(Basket)
admin.site.register(Library)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('name',)
    # readonly_fields = ('image', 'short_description')

class BasketAdmin(admin.TabularInline):
    model = Basket
    readonly_fields = ('created_timestamp',)
    filter = ('product','created_timestamp')

