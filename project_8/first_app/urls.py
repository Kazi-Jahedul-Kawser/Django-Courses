from django.urls import path
from first_app.views import signup, home ,profile, Userlogin, user_logout, change_pass, reset_pass, change_user


urlpatterns = [
    path('signup/',signup, name='signup'),
    path('logout/',user_logout, name='logout'),
    path('login/',Userlogin, name='login'),
    path('profile/',profile, name='profile'),
    path('change_pass/',change_pass, name='change_pass'),
    path('reset_pass/',reset_pass, name='reset_pass'),
    path('change_user/',change_user, name='change_user'),
    path('',home, name='home')
]
