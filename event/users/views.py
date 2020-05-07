from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Profile, Event, City, Tag
from .forms import CityForm, SportForm, EventForm
# Create your views here.

def index(request):
	events = Event.objects.all()
	context = {'events': events, }
	return render(request, 'index.html', context=context)


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password = password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	context = {'form': form}
	return render(request, 'register.html', context=context)

def users(request):
	profiles = Profile.objects.all()
	context = {'profiles': profiles}

	return render(request, 'users.html', context=context)

@login_required
def profile(request):
    return render(request, 'profile.html')

def cities(request):
	cities = City.objects.all()
	context = {'cities': cities}
	return render(request, 'cities.html', context=context)

def sports(request):
	sports = Tag.objects.all()
	context = {'sports': sports}
	return render(request, 'sports.html', context=context)

def event_detail(request, slug):
	event = Event.objects.get(slug__iexact=slug)
	return render(request, 'event_detail.html', context= {'event': event})

def profile_detail(request, id):
	profile = Profile.objects.get(id__iexact=id)
	return render(request, 'profile_detail.html', context= {'profile': profile})

def city_detail(request, slug):
	city = City.objects.get(slug__iexact=slug)
	return render(request, 'city_detail.html', context= {'city': city})

def tag_detail(request, slug):
	tag = Tag.objects.get(slug__iexact=slug)
	return render(request, 'tag_detail.html', context= {'tag': tag})

@login_required
def add_city(request):
	if request.method == 'POST':
		form = CityForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = CityForm()

	return render(request, 'add_city.html', {'form': form})

@login_required
def add_sport(request):
	if request.method == 'POST':
		form = SportForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = SportForm()

	return render(request, 'add_sport.html', {'form': form})

@login_required
def add_event(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = EventForm()

	return render(request, 'add_event.html', {'form': form})

@login_required
def add_user_event(request, slug):
	event = Event.objects.get(slug__iexact=slug)
	request.user.profile.profile_events.add(event)
	event.participants.add(request.user.profile)
	event.save()

	return redirect('index')
	#login(request, user)
	#if not event in profile.profile_events.all():
	#user.profile.profile_events.add(event)
	#profile.profile_events.add(event)

	#return redirect('profile')








