from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.shortcuts import reverse

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=150)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
	contact = models.CharField(max_length=150, default='unknown')
	profile_events = models.ManyToManyField('Event', blank=True, related_name='profiles')

	def __str__(self):
		return self.user.username + ' Profile'

	def get_absolute_url(self):
		return reverse('profile_detail_url', kwargs={'id': self.id})


class Event(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField(default='No description')
	total_participants = models.IntegerField()
	current_participants = models.IntegerField(default=1)
	time = models.DateTimeField()
	contact = models.CharField(max_length=150, default='unknown')
	slug = models.SlugField(max_length=150, unique=True)
	tags = models.ManyToManyField('Tag', blank=True, related_name='events')
	city = models.ManyToManyField('City', blank=True, related_name='events')
	participants = models.ManyToManyField('Profile', blank=True, related_name='events')

	def __str__(self):
		return self.title 

	def get_absolute_url(self):
		return reverse('event_detail_url', kwargs={'slug': self.slug})

	class Meta:
		ordering = ['-time']


class Tag(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, blank=True, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('tag_detail_url', kwargs={'slug': self.slug})

	class Meta:
		ordering = ['-title']

class City(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, blank=True, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('city_detail_url', kwargs={'slug': self.slug})

	class Meta:
		ordering = ['-title']

