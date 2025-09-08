from django.urls import path
from author.views import add_author
urlpatterns = [
    path('add_author/', add_author, name="add_author")
]
