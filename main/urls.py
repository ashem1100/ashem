from django.urls import path
from main.views import *
app_name = 'main'
urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('credentials/',credentials,name='credentials'),

]