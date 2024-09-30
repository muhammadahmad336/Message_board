from django.shortcuts import render

from .models import post
# Create your views here.
def homeView(request):
    posts_list = post.objects.all()

    for posts in posts_list:
        print(posts_list)
        print("ahmad")
    return render(request, 'index.html',{
        "posts": posts_list,
        "test" : 'This is Testing STR'
    })