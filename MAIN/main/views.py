from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post
from .utils import update_views


def home(request):
    return render(request, "forums.html", {})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post":post
    }
    
    update_views (request, post)
    return render(request, "detail.html", context)


def posts(request, slug):
    category = get_object_or_404(Category, slug)
    posts = Post.objects.filter(approved=True, categories=category)

    context = {
        "posts":posts,
    }

    return render(request, "posts.html", {})