from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('users', views.users, name='users'),
    path('cities', views.cities, name='cities'),
    path('add_city', views.add_city, name='add_city'),
    path('add_sport', views.add_sport, name='add_sport'),
    path('add_event', views.add_event, name='add_event'),
    path('sports', views.sports, name='sports'),
    path('profile', views.profile, name='profile'),
    path('event/<str:slug>/', views.event_detail, name='event_detail_url'),
    path('profile/<str:id>/', views.profile_detail, name='profile_detail_url'),
    path('city/<str:slug>/', views.city_detail, name='city_detail_url'),
    path('tag/<str:slug>/', views.tag_detail, name='tag_detail_url'),
    path('s/<str:slug>/', views.add_user_event, name='add_user_event')
]
