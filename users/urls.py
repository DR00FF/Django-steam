from django.urls import path
from users.views import login, register, profile, logout,  profile_edit_view

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'), #добавил
    path('logout/', logout, name='logout'),
    path('profile/edit/', profile_edit_view, name='profile_edit')

]