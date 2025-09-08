from django.urls import path 
from musicians.views import add_musicians, edit_musicians
urlpatterns = [
    path('add/', add_musicians, name='musicians'),
    path('edit/<int:id>', edit_musicians, name='edit_musicians')
]
