from django.shortcuts import render, redirect
from album.forms import Add_Album
from album.models import Album
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album = Add_Album(request.POST)
        if album.is_valid():
            album.save()
            return redirect('album')
    else:
        album = Add_Album()
    return render(request, 'album.html', {'album':album})

def edit_album(request, id):
    album_instance = Album.objects.get(pk=id)
    if request.method == 'POST':
        album = Add_Album(request.POST, instance=album_instance)
        if album.is_valid():
            album.save()
            return redirect('home')
    else:
        album = Add_Album(instance=album_instance)
    return render(request, 'album.html', {'album':album})

def delete_album(request, id):
    album_instance = Album.objects.get(pk=id)
    album_instance.delete()
    return redirect('home')