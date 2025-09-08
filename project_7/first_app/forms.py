from django import forms
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels ={
            'name':'Student Name ',
            'roll' : 'Student Roll ',
            'father' : "Father's Name",
            'address' : "Student's Address: "
        }
        
        widgets ={
            'name': forms.TextInput(attrs={'placeholder':"Enter Student Name", 'class':"form-label"}),
            'father': forms.TextInput(attrs={'placeholder':"Enter Student's Father Name", 'class':"form-label"}),
            'address': forms.TextInput(attrs={'placeholder':"Enter Student's Address", 'class':"form-label"}) 
        }
        
        help_texts ={
            'name' : "name should be all capital letter"
        }
        
        error_messages = {
            'name' : {'required' : 'Name is required'}
        }