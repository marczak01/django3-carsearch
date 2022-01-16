from .models import Advert, Brand
from django.db.models import Q


def searchAdverts(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    brands = Brand.objects.filter(name__icontains=search_query)

    adverts = Advert.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(brand__in=brands)
    )

    return adverts, search_query