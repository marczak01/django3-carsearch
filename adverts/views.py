
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Advert, Profile
from .forms import ProjectForm

def adverts(request):
    adverts = Advert.objects.all()
    context = {'adverts': adverts}
    return render(request, 'adverts/adverts.html', context)

def advert(request, pk):
    projectObj = Advert.objects.get(id=pk)
    profile = Profile.objects.all()
    context = {'advert': projectObj, 'profile': profile}
    return render(request, 'adverts/single-advert.html', context)


@login_required(login_url="login")
def createAdvert(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adverts')

    context = {'form': form}
    return render(request, 'adverts/advert_form.html', context)


@login_required(login_url="login")
def updateAdvert(request, pk):
    advert = Advert.objects.get(id=pk)
    form = ProjectForm(instance=advert)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=advert)
        if form.is_valid():
            form.save()
            return redirect('adverts')

    context = {'form': form}
    return render(request, 'adverts/advert_form.html', context)


@login_required(login_url="login")
def deleteAdvert(request, pk):
    advert = Advert.objects.get(id=pk)
    if request.method == 'POST':
        advert.delete()
        return redirect('adverts')
    context = {'object': advert}
    return render(request, 'adverts/delete_template.html', context)