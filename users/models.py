from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):

    SELLER = [
        ('All','All'),
        ('Dealer','Dealer'),
        ('Private','Private'),
    ]
    #profile is deleted when we delete user. CASCADE
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    location_city = models.CharField(max_length=50, null=True, blank=False)
    location_country = models.CharField(max_length=50, null=True, blank=False)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    seller = models.CharField(max_length=200, null=True, blank=False, choices=SELLER)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


