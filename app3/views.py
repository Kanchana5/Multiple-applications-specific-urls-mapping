from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app3_first(request):
    return render(request,'app3_first.html')

def app3_second(request):
    return render(request,'app3_second.html')

def app3_third(request):
    return HttpResponse('<h1>this is my first STRING in app3</h1>')
