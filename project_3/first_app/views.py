from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author':'Rafi', 'age': 22,'lst':['python','is','best'],'date':datetime.datetime.now(),'courses':[
        {
            'id' :1,
            'name' : 'python',
            'fee' : 5000
        },
        {
            'id' :2,
            'name' : 'java',
            'fee' : 6000
        },
        {
            'id' :3,
            'name' : 'C',
            'fee' : 4000
        }
    ]}
    return render(request,'home.html',d)