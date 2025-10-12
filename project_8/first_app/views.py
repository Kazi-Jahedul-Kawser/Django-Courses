from django.shortcuts import render, redirect
from first_app.forms import UserRegister, ChangeUser
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserRegister(request.POST)
            if form.is_valid() :
                messages.success(request, 'Successfully Created an Account')
                messages.warning(request, 'This is Warning Message')
                messages.info(request, 'This is Info Messege')
                form.save()
        else:
            form = UserRegister()
                
        return render(request,'signup.html', {'form':form})
    else:
        return redirect('profile')

def Userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user=user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    else:
        return redirect('profile')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = ChangeUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # refresh with new data
    else:
        form = ChangeUser(instance=request.user)

    return render(request, 'profile.html', {'form': form})


    
    

def user_logout(request):
    logout(request)
    return redirect('login')
        
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html', {'user':request.user})
    else:
        return redirect('profile')

def change_pass(request):
    if request.method == "POST":
        form = PasswordChangeForm(user= request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html', {'form':form})
def reset_pass(request):
    if request.method == "POST":
        form = SetPasswordForm(user= request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'change_pass.html', {'form':form})

def change_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUser(request.POST, instance = request.user)
            if form.is_valid():
                form.save()
        else:
            form = ChangeUser()
        return render(request, 'profile.html', {'form':form})
    else:
        redirect('login')

