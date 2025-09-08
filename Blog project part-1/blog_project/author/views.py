from django.shortcuts import render, redirect
from . import forms  
# Create your views here.
def add_author(request):
    if request.method == 'POST':
        add_author = forms.AuthorForm(request.POST)
        if add_author.is_valid():
            add_author.save()
            return redirect('add_author')
    
    else:
        add_author = forms.AuthorForm(request.POST)
    
    return render(request, 'author.html', {'form':add_author})