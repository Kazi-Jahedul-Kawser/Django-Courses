from django import forms
from musicians.models import Musicians
class Add_Musicians(forms.ModelForm):
    class Meta:
        model = Musicians
        fields = '__all__'
        labels = {
            'first_name' : 'First Name ',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'number' : 'Phone Number',
            'instrument':'Instruments'
        }