from django.urls import path
from first_app.views import home, get_cookies, del_cookies, set_session, get_session, del_session
urlpatterns = [
    path('', set_session),
    path('get/', get_session),
    path('del/', del_session),
    
]
