from django.urls import path 
from . import views

urlpatterns =[
    #criei página inicial q eu mesmo fiz
    path('', views.index, name='index'), 
]