from django.urls import path

from . import views


# our-domain.com/  -> loading the index function
# our-domain.com/home -> loading the index function
urlpatterns = [
  path('', views.index), 
  path('home', views.index ),
]