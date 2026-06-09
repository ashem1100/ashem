from django.db import models

# Create your models here.
class BaseInformation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    profile = models.ImageField(upload_to='info/', default='info/defaultprofile.jpg')
    cv =models.FileField(upload_to='info/doc/', null=True)
    github_link = models.URLField(blank=True, null=True)
    telegram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    x_link =models.URLField(blank=True, null=True)
    about = models.TextField(null=True)
    def __str__(self):
        return self.name


class JobExperienceInformation(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    about = models.TextField(null=True)
    time_start = models.CharField(max_length=100)
    time_end = models.CharField(max_length=100, default='تاکنون')
    def __str__(self):
        return self.title


class EducationInformation(models.Model):
    title = models.CharField(max_length=100)
    academy = models.CharField(max_length=100)
    time_start = models.CharField(max_length=100)
    time_end = models.CharField(max_length=100, default='تاکنون')

    def __str__(self):
        return self.title

class SkillInformation(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class CertificateInformation(models.Model):
    title = models.CharField(max_length=100)
    certificator = models.CharField(max_length=100)
    date = models.DateField(null=True)
    def __str__(self):
        return self.title