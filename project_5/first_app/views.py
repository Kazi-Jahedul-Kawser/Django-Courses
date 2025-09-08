from django.shortcuts import render
from . forms import contactForm, StudentForm, PasswordValidation
# Create your views here.
def home(request):
    return render(request , "./first_app/home.html")

def about(request):
    if(request.method == 'POST'):
        name = request.POST.get('username')
        email = request.POST.get('usermail')
        return render(request , "./first_app/about.html", {'name' : name, 'email':email })

def form(request):
    print(request.POST)
    return render(request , "./first_app/form.html")

def djangoForm(request):
    form = contactForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open ('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    
    else:
        form = contactForm()
    return render(request, './first_app/forms.html', {'form': form})


def studentForm(request):
    stForm = StudentForm(request.POST, request.FILES)
    if request.method == 'POST':
        if stForm.is_valid():
            print(stForm.cleaned_data)
    
    return render(request, './first_app/student_form.html',{'stForm':stForm})

def passwordValitation(request):
    
    PassValidtation = PasswordValidation(request.POST)
    
    if request.method == "POST":
        if PassValidtation.is_valid():
            print(PassValidtation)
    return render(request, './first_app/password_valid.html', {'PassValidtation':PassValidtation})