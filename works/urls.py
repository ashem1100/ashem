from django.urls import path, include
from works.views import *

app_name = 'works'
urlpatterns = [
    path('', worksindex, name='worksindex'),
]