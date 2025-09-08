
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('path/', views.form, name='form'),
    path('djangoForm/', views.djangoForm, name='djangoForm'),
    path('studentForm/', views.studentForm, name='studentForm'),
    path('passwordValid/', views.passwordValitation, name='passValid')
]