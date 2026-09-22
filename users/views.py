from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from products.models import Library



# Create your views here.
def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))

    else:
        form = UserLoginForm()

    context = {
        "title": "Login | Game Store",
        "form": form
    }
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()

    context = {
        "title": "Register | Game Store",
        "form": form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
   total_quantity = sum(1 for game in Library.objects.filter(user=request.user))
   if request.method == 'POST':
       form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('users:profile'))
       else:
           print(form.errors)

   else:
       form = UserProfileForm(data=request.POST)

   context = {
       "title": "Profile | Game Store",
       "form": form,
       "total_quantity": total_quantity
   }
   return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile_edit_view(request):
    """Страница редактирования профиля."""
    if request.method == 'POST':
        user = request.user
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_image = request.FILES.get('image')
        new_banner = request.FILES.get('banner')

        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email
        if new_image:
            user.image = new_image
        if new_banner:
            user.banner = new_banner

        user.save()
        return HttpResponseRedirect(reverse('users:profile'))
    context = {
        "title": "RedactProfile | Game Store",
    }
    return render(request, 'users/profile_edit.html', context)