from django.shortcuts import render, redirect
from posts.forms import PostForm
from posts.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_post(request):
    if request.method =='POST': 
        add_post = PostForm(request.POST)
        if add_post.is_valid():
            add_post.instance.author =request.user
            add_post.save()
            return redirect("home")
    else:
        add_post = PostForm()
    
    return render(request,'add_post.html', {'add_post': add_post})
@login_required
def edit_post(request,id):
    post = Post.objects.get(pk=id)
    if request.method =='POST': 
        add_post = PostForm(request.POST, instance=post)
        if add_post.is_valid():
            add_post.instance.author = request.user
            add_post.save()
            return redirect("my_blogs")
    else:
        add_post = PostForm(instance = post)
    return render(request,'add_post.html', {'add_post': add_post})
@login_required            
def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("my_blogs")
