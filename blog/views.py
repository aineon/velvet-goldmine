from django.shortcuts import render
from .models import BlogPost


def all_posts(request):
    """A view to show all blog posts"""
    posts = BlogPost.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)
