from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return render(request,'app2_first.html')

def app2_second(request):
    return render(request,'app2_second.html')

def app2_three(request):
    return HttpResponse('<h1>This is my first STRING in App2</h1>')
