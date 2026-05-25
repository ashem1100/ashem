from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blogindex(request):
    return render(request, 'blog/blog.html')

def post(request):
    return render(request, 'blog/blog-details.html')