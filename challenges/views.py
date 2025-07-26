from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view is a function/class

def index(request):
    return HttpResponse("This Works!")


