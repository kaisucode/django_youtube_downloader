from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.submit_link), name='homepage'),
]
