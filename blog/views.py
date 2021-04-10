from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import BlogPost
from .forms import BlogForm


def all_posts(request):
    """A view to show all blog posts"""
    posts = BlogPost.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def post_detail(request, post_id):
    """A view to show individual blog post"""
    post = get_object_or_404(BlogPost, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/blogpost_detail.html', context)


def add_post(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, f'Successfully added {post.title}!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request,
                           'Failed to add blog post.'
                           'Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blogpost.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
