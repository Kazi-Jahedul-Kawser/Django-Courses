from django import forms 
from task.models import Task
class Add_Task(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            'title' : 'Title',
            'description' : 'Description',
            'is_completed' : 'Is Completed',
            'date' : 'Date'
        }
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date'})
        }