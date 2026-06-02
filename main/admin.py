from django.contrib import admin
from main.models import *
# Register your models here.

class BaseInformationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    pass

class JobAdmin(admin.ModelAdmin):
    search_fields = ('title', 'company',)
    list_display = ('title', 'company',)
    list_filter = ('time_start', 'time_end',)
    pass

class EducationInformationAdmin(admin.ModelAdmin):
    search_fields = ('title', 'academy',)
    list_display = ('title', 'academy',)
    list_filter = ('time_start', 'time_end',)
    pass

class SkillInformationAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description',)
    list_display = ('title', 'description',)
    pass

class CertificateInformationAdmin(admin.ModelAdmin):
    search_fields = ('title', 'certificator',)
    list_display = ('title', 'certificator','date')
    list_filter = ('certificator', 'date')

admin.site.register(BaseInformation, BaseInformationAdmin)
admin.site.register(JobExperienceInformation, JobAdmin)
admin.site.register(EducationInformation, EducationInformationAdmin)
admin.site.register(SkillInformation, SkillInformationAdmin)
admin.site.register(CertificateInformation, CertificateInformationAdmin)