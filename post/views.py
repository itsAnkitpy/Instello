from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    # Fetching the info of the logged in user and displaying it in index.html
    user = request.user
    posts = Feed.objects.filter(user=user)
    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)
    # Show all posts in group_ids - from latest to oldest 
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')

    context = {
        'post_items':post_items,
    } 
    return render(request, 'index.html',context)