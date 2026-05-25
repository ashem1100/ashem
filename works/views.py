from django.shortcuts import render

# Create your views here.
def worksindex(request):
    return render(request, 'works/works.html')