from django.shortcuts import render
from main.models import *

info = BaseInformation.objects.all()
jobs = JobExperienceInformation.objects.all()
educations = EducationInformation.objects.all()
certificates = CertificateInformation.objects.all()
skills = SkillInformation.objects.all()

context = {
    'info': info,
    'jobs': jobs,
    'educations': educations,
    'certificates': certificates,
    'skills': skills,
}

# Create your views here.
def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def credentials(request):
    return render(request, 'credentials.html', context)