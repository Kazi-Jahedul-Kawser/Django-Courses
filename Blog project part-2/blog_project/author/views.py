from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from author.forms import RegisterForm, ChangeUser
from posts.models import Post
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Account Created Successfully')   
            return redirect('profile')
        
    else:
        form = RegisterForm()
        
    return render(request, 'register.html', {'form':form,'type':'Register'})
    

def user_login(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=name, password = user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Loggin information is incorrect')
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form':form,'type':'Login'})
    
    
@login_required
def profile(request):
    if request.method == "POST":
        form = ChangeUser(request.POST,instance= request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
        
    else:
        form = ChangeUser(instance= request.user)
    return render(request, 'profile.html', {'form':form})

@login_required    
def user_logout(request):
    logout(request)
    messages.warning(request,'Successfully Loged Out')
    return redirect('home')
@login_required 
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,user=request.user)
            messages.success(request, "Successfully Updated Password")
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password.html',{'form':form,'type':'Reset Password'})
@login_required 
def set_password(request):
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,user=request.user)
            messages.success(request, "Successfully Updated Password")
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'password.html',{'form':form, 'type':'Set Password'})

def my_blogs(request):
    post = Post.objects.filter(author=request.user)
    return render(request, 'my_blogs.html', {"post":post})
        