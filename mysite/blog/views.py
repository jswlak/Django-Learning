from django.shortcuts import render

# Create your views here.

from .models import BlogPost

def post_list(request):
    posts = BlogPost.objects.all()   # fetch all posts
    return render(request, 'blog/post_list.html', {'posts': posts})

