from symtable import Class

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    main_pic = models.ImageField(upload_to='blog/', default='blog/blog1.jpeg')
    categories = models.ManyToManyField(Category , related_name='categories')
    #tags
    views = models.IntegerField(default=0)
    class Meta:
        ordering = ('create_date',)
    def __str__(self):
        return self.title



class Tag (models.Model):
    name = models.CharField(max_length=200)
