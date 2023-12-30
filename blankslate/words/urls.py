from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('word/', views.word, name='word'),
    path('all/', views.all, name='all'),
]