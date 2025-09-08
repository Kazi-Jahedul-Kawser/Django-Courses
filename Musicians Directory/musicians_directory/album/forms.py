from django import forms
from album.models import Album

class Add_Album(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        label = {
            'name' : 'Album Name: ',
            'musician' : 'Musician',
            'date' : 'Date',
            'rating' : 'Rating'
        }
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date'}),
            'rating':forms.Select()
            
        }