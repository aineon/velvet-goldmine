from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def all_posts(request):
    """A view to show all blog posts"""
    posts = BlogPost.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/blogpost_detail.html', context)
