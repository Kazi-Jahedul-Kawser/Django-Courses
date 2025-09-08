from django import forms
from categories.models import Categories
class Add_Categories(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
        labels = {
            'name':'Category Name'
        }