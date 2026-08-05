from django.urls import path
from products.views import catalog

app_name = 'products'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', catalog, name='home'),
    # path('products', catalog, name='catalog'),
    # path('about_us', about, name='about')
]