from django import template

from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/latest-posts.html')
def latestPosts():
    posts = Post.objects.filter(status=1).order_by('-publish_date')[:5]
    return {'posts': posts}
