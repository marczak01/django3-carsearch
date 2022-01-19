from django.db.models import Q
from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Advert, Profile, Brand
from .forms import ProjectForm
from .utils import searchAdverts

def adverts(request):
    page = 'adverts'
    search_query = ""

    #searching
    if request.GET.get('search_query'):
        adverts, search_query = searchAdverts(request)
    else:
    #sorting
        adverts = Advert.objects.all()
        sort_by = request.GET.get('sort')

        if sort_by == 'new':
            adverts = adverts.order_by('-created')
        elif sort_by == 'old':
            adverts = adverts.order_by('created')
        elif sort_by == 'price_low':
            adverts = adverts.order_by('price')
        elif sort_by == 'price_high':
            adverts = adverts.order_by('-price')
        elif sort_by == 'mileage_low':
            adverts = adverts.order_by('mileage')
        elif sort_by == 'mileage_high':
            adverts = adverts.order_by('-mileage')
        else:
            adverts = adverts.order_by('-created')

    num = len(adverts)
    context = {'adverts': adverts, 'num': num, 'page': page, 'search_query': search_query}
    return render(request, 'adverts/adverts.html', context)



def advert(request, pk):
    page = 'advert'
    advert = Advert.objects.get(id=pk)
    profile = Profile.objects.all()
    context = {'advert': advert, 'profile': profile, 'page': page}
    return render(request, 'adverts/single-advert.html', context)



@login_required(login_url="login")
def createAdvert(request):
    profile = request.user.profile #aktualnie zalogowany uzytk
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            #set current user to owner while creating advert
            advert = form.save(commit=False)
            advert.owner = profile
            advert.save()
            return redirect('adverts')

    context = {'form': form}
    return render(request, 'adverts/advert_form.html', context)



@login_required(login_url="login")
def updateAdvert(request, pk):
    profile = request.user.profile
    advert = profile.advert_set.get(id=pk)
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
    profile = request.user.profile
    advert = profile.advert_set.get(id=pk)
    if request.method == 'POST':
        advert.delete()
        return redirect('adverts')
    context = {'object': advert}
    return render(request, 'adverts/delete_template.html', context)