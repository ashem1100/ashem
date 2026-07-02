from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import *

# Create your views here.
def blogindex(request, cat=None, author=None):
    posts = Post.objects.filter(status=True)
    if cat:
        posts = posts.filter(categories__name=cat)
    elif author:
        posts = posts.filter(author__username=author)
    categories = Category.objects.filter(parent=None)
    context = {'posts': posts , 'categories': categories}
    return render(request, 'blog/blog.html', context)

def viewpost(request, id):
    post = Post.objects.filter(status=True)
    context = {'post': get_object_or_404(post, id=id)}
    return render(request, 'blog/blog-details.html', context)
