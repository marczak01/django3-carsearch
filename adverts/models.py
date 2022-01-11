from django.db import models
import uuid

from django.db.models.fields import DateTimeCheckMixin, DateTimeField
from users.models import Profile
# Create your models here.


class Advert(models.Model):

    YES_OR_NO = [
        ('Y','Yes'),
        ('N','No'),
    ]

    MAN_AUTO = [
        ('M','Manual'),
        ('A','Automatic'),
    ]

    SELLER = [
        ('A','All'),
        ('D','Dealer'),
        ('P','Private'),
    ]

    DOORS = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    ]

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=False)
    featured_image = models.ImageField(null=True, blank=False)
    brand = models.ForeignKey('Brand', null=True, on_delete=models.DO_NOTHING)
    variant = models.CharField(max_length=200, null=True, blank=False)
    fuel_type = models.ForeignKey('Fuel', null=True, on_delete=models.DO_NOTHING)
    year_of_production = models.IntegerField(null=True, blank=False)
    engine_capacity = models.CharField(max_length=200, null=True, blank=False)
    power = models.CharField(max_length=200, null=True, blank=False)
    mileage = models.CharField(max_length=200, null=True, blank=False)
    seller = models.CharField(max_length=200, null=True, blank=False, choices=SELLER)
    first_owner = models.CharField(max_length=200, null=True, blank=False, choices=YES_OR_NO)
    broken = models.CharField(max_length=200, null=True, blank=False, choices=YES_OR_NO)
    no_crashed = models.CharField(max_length=200, null=True, blank=False, choices=YES_OR_NO)
    manual_auto = models.CharField(max_length=200, null=True, blank=False, choices=MAN_AUTO)
    color = models.CharField(max_length=200, null=True, blank=False)
    num_of_doors = models.IntegerField(null=True, blank=False, choices=DOORS)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title



class Brand(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name



class Fuel(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name