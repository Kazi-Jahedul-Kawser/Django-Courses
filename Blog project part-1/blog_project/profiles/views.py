from django.shortcuts import render, redirect
from . import forms  
# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        add_profile = forms.ProfileForm(request.POST)
        if add_profile.is_valid():
            add_profile.save()
            return redirect('add_profile')
    
    else:
        add_profile = forms.ProfileForm(request.POST)
    
    return render(request, 'profile.html', {'form':add_profile})