from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from post.forms import NewPostform
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


def NewPost(request):
    user = request.user.id
    # profile = get_object_or_404(Profile, user=user)
    tags_obj = []
    
    if request.method == "POST":
        form = NewPostform(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tags')
            tag_list = list(tag_form.split(','))

            for tag in tag_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_obj.append(t)
            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user_id=user)
            p.tags.set(tags_obj)
            p.save()
            return redirect('home')
    else:
        form = NewPostform()
    context = {
        'form': form
    }
    return render(request, 'newpost.html', context)


def PostDetail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    

    context = {
        'post': post,
        
    }

    return render(request, 'postdetail.html', context)