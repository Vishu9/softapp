from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

# Create your views here.
def index_view(request):    

    return render(request,'index.html')