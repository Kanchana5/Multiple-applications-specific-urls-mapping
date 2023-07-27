from django.urls import path
from app3.views import *
app_name='app3'

urlpatterns=[
    path('app3_first/',app3_first,name='app3_first'),
    path('app3_second/',app3_second,name='app3_second'),
    path('app3_third/',app3_third,name='app3_third'),
]