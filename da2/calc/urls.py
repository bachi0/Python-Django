from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('multiply', views.multiply, name='multiply')
]
