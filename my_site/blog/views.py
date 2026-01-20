from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "hike-the-mountains",
        "image": "forest.png",
        "author": "InnoCoda",
        "date": date(2026, 1, 19),
        "title": "Dasert",
        "excerpt": "There's nothing like the viewa you get when hiking in the moutain",
        "content": """ My goal is to keep on growing as a developer - and if i could 
                                help you do the same, I'd be very happy!""",
    },
    {
        "slug": "programing",
        "image": "innocoda.png",
        "author": "InnoCoda",
        "date": date(2026, 1, 9),
        "title": "God's Wills",
        "excerpt": "They is all ways God by my side all time ",
        "content": """ My goal is to keep on growing as a developer - and if i could 
                                help you do the same, I'd be very happy!""",
    },
    {
        "slug": "Coding-is-life",
        "image": "image.png",
        "author": "InnoCoda",
        "date": date(2026, 1, 19),
        "title": "Coding is life",
        "excerpt": "There's nothing like seeing your, code making you money ",
        "content": """ My goal is to keep on growing as a developer - and if i could 
                                help you do the same, I'd be very happy!""",
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_posts = sorted_post[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identiend_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post": identiend_post})
