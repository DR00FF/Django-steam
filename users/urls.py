from django.urls import path
from users.views import login, register, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'), #добавил
    path('logout/', profile, name='logout'),
]