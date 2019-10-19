from django.urls import path
from . import views

app_name='searchstore'

urlpatterns = [
		path('', views.searchResult, name='searchResult'),
]