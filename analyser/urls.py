from django.urls import path
from . import views

app_name = 'analyser'

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
]