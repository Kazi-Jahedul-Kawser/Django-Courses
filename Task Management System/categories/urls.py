from django.urls import path
from categories.views import add_categories
urlpatterns = [
    path('add/', add_categories, name='category')
]
