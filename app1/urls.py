from django.urls import path
from app1.views import *
app_name='app1'

urlpatterns=[
    path('app1_first/',app1_first,name='app1_first'),
    path('app1_second/',app1_second,name='app1_second'),
    path('app1_three/',app1_three,name='app1_three'),

]