from django.urls import path 
from album.views import add_album, edit_album, delete_album
urlpatterns = [
    path("add/", add_album, name='album'),
    path('edit/<int:id>',edit_album, name='edit'),
    path('delete/<int:id>',delete_album, name='delete')
]
