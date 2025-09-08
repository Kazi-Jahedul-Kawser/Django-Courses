from django.shortcuts import render, redirect
from posts.forms import PostForm
from posts.models import Post
# Create your views here.
def add_post(request):
    if request.method =='POST': 
        add_post = PostForm(request.POST)
        if add_post.is_valid():
            add_post.save()
            return redirect("home")
    else:
        add_post = PostForm()
    
    return render(request,'add_post.html', {'add_post': add_post})

def edit_post(request,id):
    post = Post.objects.get(pk=id)
    add_post = PostForm(instance = post)
    if request.method =='POST': 
        add_post = PostForm(request.POST)
        if add_post.is_valid():
            add_post.save()
            return redirect("home")
    else:
        add_post = PostForm(instance = post)
    return render(request,'add_post.html', {'add_post': add_post})
            
def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("home")
    # add_post = PostForm(instance = post)
    # if request.method =='POST': 
    #     add_post = PostForm(request.POST)
    #     if add_post.is_valid():
    #         add_post.save()
    #         return redirect("home")
    # else:
    #     add_post = PostForm(instance = post)
    # return render(request,'add_post.html', {'add_post': add_post})    