
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('searchwithautoescape', views.search, {'autoescape': True}),
    path('searchwithoutautoescape', views.search, {'autoescape': False}),
]
