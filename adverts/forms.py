from django.forms import ModelForm
from .models import Advert
from django.utils.translation import gettext_lazy as _

class ProjectForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'description', 'featured_image', 'brand', 'variant',
                  'fuel_type', 'year_of_production', 'price', 'engine_capacity',
                  'power', 'mileage', 'seller', 'first_owner', 'broken', 'no_crashed', 
                  'manual_auto', 'color', 'num_of_doors']
        labels = {
            'featured_image': _('Photos'),
            'broken': _('Is car broken or something?'),
            'no_crashed': _('Has the car been in an accident?'),
            'manual_auto': _('Manual or Automatic'),
            'num_of_doors': _('Number of doors'),
        }