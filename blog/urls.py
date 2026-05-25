from django.urls import path,include
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('',blogindex,name='blogindex'),
    path('post/',post,name='post'),

]