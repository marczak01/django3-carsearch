
from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Advert, Profile
from .forms import ProjectForm

def adverts(request):
    page = 'adverts'
    adverts = Advert.objects.all()
    sort_by = request.GET.get('sort')

    if sort_by == 'new':
        adverts = Advert.objects.all().order_by('-created')
    elif sort_by == 'old':
        adverts = Advert.objects.all().order_by('created')
    elif sort_by == 'mileage-high':
        adverts = Advert.objects.all().order_by('-mileage')
    elif sort_by == 'mileage-low':
        adverts = Advert.objects.all().order_by('mileage')
    elif sort_by == 'power-high':
        adverts = Advert.objects.all().order_by('-power')
    elif sort_by == 'power-low':
        adverts = Advert.objects.all().order_by('power')
    else:
        adverts = Advert.objects.all().order_by('-created')

    num = len(adverts)

    context = {'adverts': adverts, 'num': num, 'page': page}

    return render(request, 'adverts/adverts.html', context)

def advert(request, pk):
    page = 'advert'
    projectObj = Advert.objects.get(id=pk)
    profile = Profile.objects.all()
    context = {'advert': projectObj, 'profile': profile, 'page': page}
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