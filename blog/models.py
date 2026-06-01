from symtable import Class

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    #author
    #main pic
    #categories
    #tags
    #views
    class Meta:
        ordering = ('create_date',)
    def __str__(self):
        return self.title

class Category (models.Model):
    name = models.CharField(max_length=200)
    #parent


class Tag (models.Model):
    name = models.CharField(max_length=200)
