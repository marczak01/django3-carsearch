from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('', views.adverts, name="adverts"),
    path('advert/<str:pk>/', views.advert, name="single-advert"),
    path('create-advert/', views.createAdvert, name="advert_form"),
    path('update-advert/<str:pk>/', views.updateAdvert, name="advert_form"),
    path('delete-advert/<str:pk>/', views.deleteAdvert, name="delete-advert")
]