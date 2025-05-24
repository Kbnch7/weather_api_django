from django.urls import path

from .views import show_weather

urlpatterns = [
    path('', show_weather, name='homepage')
]