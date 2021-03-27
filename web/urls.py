from django.urls import path, include
from django.views import generic
from . views import index_view

app_name = 'web'

urlpatterns = [
    path('',index_view, name= 'index'),
]