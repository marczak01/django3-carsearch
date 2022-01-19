from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Profile
from .forms import CustomUserCreationForm, ProfileForm

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created!")

            login(request, user)
            return redirect('edit-account')

        else:
            messages.success(request, "An error has ocured furing registration")

    context = {'page': page, 'form': form}
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


def profile(request, pk):
    page = 'profile'
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile, 'page': page}
    return render(request, 'users/account.html', context)



@login_required(login_url="login")
def userAccount(request):
    page = 'account'
    profile = request.user.profile

    adverts = profile.advert_set.all()

    context = {'profile': profile, 'adverts': adverts, 'page': page}
    return render(request, 'users/account.html', context)



@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)