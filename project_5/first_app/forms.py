from django import forms
from django.core import validators
class contactForm(forms.Form):
    name = forms.CharField(label='User Name :', help_text='Name must be 8 words', widget = forms.Textarea(attrs={'placeholder': 'Enter Your Name', 'id': 'text_area'}))
    # file = forms.FileField()
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    balance = forms.DecimalField()
    date = forms.DateField(label='Date: ', widget=forms.DateInput(attrs={'type':'date'}))
    apointment = forms.DateTimeField(label='Apoinment : ', widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    choise = forms.BooleanField()
    CHOISE =[('S','Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOISE, widget = forms.RadioSelect)
    TYPE = [('P', 'Papperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    Pizza = forms.MultipleChoiceField(choices=TYPE, widget= forms.CheckboxSelectMultiple)
    
    
# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)
    
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
        
#         if(len(valname) < 10):
#             raise forms.ValidationError('Name must be 10 character')
#         if('.com' not in valemail):
#             raise forms.ValidationError('Your email must contain .com')
        
class StudentForm(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,message='Name will be atleast 10 character.')])
    email = forms.EmailField(widget=forms.EmailInput)
    age = forms.IntegerField(validators=[validators.MinValueValidator(18, message='Age must be atleast 18+'),validators.MaxValueValidator(50, message='Age must be less than 50')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['jpg'], message='Input valid File')])
    
    
class PasswordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_pass = forms.CharField(widget=forms.PasswordInput)
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valpass = self.cleaned_data['password']
    #     conpass = self.cleaned_data['confirm_pass']
        
    #     if(valpass != conpass):
    #         raise forms.ValidationError('Password wrong')
    
    def clean(self):
        
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        conPass = self.cleaned_data['confirm_pass']
        if(valpass != conPass):
            raise forms.ValidationError("password doesn't match!")