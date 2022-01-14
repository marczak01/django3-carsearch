from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Profile

def registerUser(request):
    page = 'register'
    context = {'page': page}
    return render(request, 'users/login_register.html', context)


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('adverts')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('adverts')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.error(request, 'User is logout!')
    return redirect('login')


def profile(request):
    profile = Profile.objects.all()
    context = {'profiles': profile}
    return render(request, 'users/profile.html', context)