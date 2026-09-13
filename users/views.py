from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required



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
        "form": form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
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
       "form": form
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

        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email
        if new_image:
            user.image = new_image

        user.save()
        return HttpResponseRedirect(reverse('users:profile'))

    return render(request, 'users/profile_edit.html')