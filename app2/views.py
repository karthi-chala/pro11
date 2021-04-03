from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>welcome to index of app2</h>')

def sample(request):
    return render(request,'app2/sample.html')

# Create your views here.
