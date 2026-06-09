from django.contrib import admin
from blog.models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'status', 'publish_date', 'update_date')
    list_filter = ('status', 'author')
    search_fields = ('title', 'author__username', 'author__first_name', 'author__last_name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)