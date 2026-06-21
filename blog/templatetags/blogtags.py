from itertools import count

from django import template

from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/latest-posts.html')
def latestPosts():
    posts = Post.objects.filter(status=1).order_by('-publish_date')[:5]
    return {'posts': posts}



@register.inclusion_tag('blog/sidebar-categories.html')
def sidebarCategories():
    categories = Category.objects.all()
    posts = Post.objects.filter(status=1)
    active_categories = {}
    for category in categories:
        active_categories[category.name] = posts.filter(categories=category).count()

    active_categories = dict(sorted(active_categories.items(), key=lambda t: t[1], reverse=True))
    active_categories = {cat:count for cat,count in active_categories.items() if count > 0}
    return {'active_categories': active_categories}
