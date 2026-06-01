from django.http import HttpResponse
from django.shortcuts import render
from blog.models import *

# Create your views here.
def blogindex(request):
    posts = Post.objects.filter(status=True)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

def post(request):
    return render(request, 'blog/blog-details.html')