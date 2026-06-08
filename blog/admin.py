from django.contrib import admin
from blog.models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'status', 'publish_date', 'update_date')
    list_filter = ('status', 'author')
    search_fields = ('title','author')
admin.site.register(Post, PostAdmin)