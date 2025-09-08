from django.shortcuts import render, redirect
from categories.forms import Add_Categories
# Create your views here.
def add_categories(request):
    if request.method == 'POST':
        add_categories = Add_Categories(request.POST)
        if add_categories.is_valid():
            add_categories.save()
            return redirect('category')
    else:
        add_categories = Add_Categories()
    
    return render(request, 'category.html', {'category':add_categories})