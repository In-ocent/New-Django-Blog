from django.shortcuts import render
from datetime import date
from django.http import Http404
from . models import Post
# Create your views here.

all_posts = [

]


def starting_page(request):
    latest_posts = Post.objects.all().order_by('date')[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identiend_post = next(
        (post for post in all_posts if post['slug'] == slug), None)

    if identiend_post is None:
        return render(request, "404.html", status=404)

    return render(request, "blog\post-detali.html", {"post": identiend_post})
