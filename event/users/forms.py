from django import forms
from .models import City, Tag, Event

class CityForm(forms.ModelForm):

	class Meta:
		model = City
		fields = ('title', 'slug')


class SportForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ('title', 'slug')


class EventForm(forms.ModelForm):

	class Meta:
		model = Event
		fields = ('title', 'description', 'total_participants', 'current_participants', 
			'time', 'contact', 'slug', 'tags', 'city', 'participants')