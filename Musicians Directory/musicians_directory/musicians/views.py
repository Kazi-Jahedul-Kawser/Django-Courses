from django.shortcuts import render, redirect
from musicians.forms import Add_Musicians
from musicians.models import Musicians
# Create your views here.
def add_musicians(request):
    if request.method == "POST":
        musicians = Add_Musicians(request.POST)
        if musicians.is_valid():
            musicians.save()
            return redirect('musicians')
            
    else:
        musicians = Add_Musicians()
        
    return render(request, 'musicians.html', {'musicians':musicians})

def edit_musicians(request, id):
    musician_instance = Musicians.objects.get(pk=id)
    if request.method == "POST":
        musicians = Add_Musicians(request.POST, instance=musician_instance)
        if musicians.is_valid():
            musicians.save()
            return redirect('home')
            
    else:
        musicians = Add_Musicians(instance=musician_instance)
        
    return render(request, 'musicians.html', {'musicians':musicians})