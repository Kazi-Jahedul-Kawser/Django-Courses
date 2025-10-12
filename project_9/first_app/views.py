from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name','Jahedul',expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookies(request):
    name = request.COOKIES.get('name')
    return render(request,'get_cookies.html', {'name':name})
def del_cookies(request):
    response = render(request, 'del_cookies.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    data ={
        'name':'Ishrak',
        'title' : 'Nagar Daddy',
        'age' : 38
    }
    
    request.session.update(data)
    return render(request, 'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name')
        title = request.session.get('title')
        request.session.modified = True
        return render(request, 'get_session.html', {'name':name, 'title':title})
    else:
        return HttpResponse('Session Login Expired. Please log in again')

def del_session(request):
    del request.session['name']
    request.session.flash()
    return render (request, 'del_session.html')