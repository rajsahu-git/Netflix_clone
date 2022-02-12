from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
AGE_CHOICES=(
    ('ALL','ALL'),
    ('Kids',"Kids")
)

# MOVIE_CHOICES=[
#     ('R','ROMANTIC'),
#     ('H','HORROR'),
#     ('C','COMEDY'),
#     ('D','DHRAMA'),
#     ('A','ACTIONS'),
#     ('S','SCIENCE_FICTION'),
# ]
MOVIE_CHOICES=(
    ('seasonal','seasonal'),
    ('single','single')
)

class CustomUser(AbstractUser):
    profile = models.ManyToManyField('Profile',blank=True)

class Profile(models.Model):
    name=models.CharField(max_length=255)
    # age_limit = models.CharField(choices=AGE_CHOICES,max_length=10)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    movie_type = models.CharField(choices=MOVIE_CHOICES,max_length=20)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    video = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyer')
    age_limit = models.CharField(choices=AGE_CHOICES,max_length=10)

class Video(models.Model):
    title=models.CharField(max_length=255,blank=True,null=True)
    file = models.FileField(upload_to='movies')


