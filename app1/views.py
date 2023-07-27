from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_first(request):
    return render(request,'app1_first.html')

def app1_second(request):
    return render(request,'app1_second.html')

def app1_three(request):
    return HttpResponse('<h2>This is my first STRING in app1</h2>')

