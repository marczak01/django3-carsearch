from django.forms import ModelForm
from .models import Advert
from django.utils.translation import gettext_lazy as _

class ProjectForm(ModelForm):
    class Meta:
        model = Advert
        fields = '__all__'
        labels = {
            'featured_image': _('Photos'),
            'broken': _('Is car broken or something?'),
            'no_crashed': _('Has the car been in an accident?'),
            'manual_auto': _('Manual or Automatic'),
            'num_of_doors': _('Number of doors'),
        }