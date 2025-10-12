from django.urls import path
from posts.views import add_post, AddPostCreateView, EditPostUpdateView, DeletePostDeleteView, DetailPostView
from posts.views import edit_post, delete_post
urlpatterns = [
    path("add/", AddPostCreateView.as_view(), name='add_post'),
    path("edit/<int:id>", EditPostUpdateView.as_view(), name='edit_post'),
    path("delete/<int:id>", DeletePostDeleteView.as_view(), name='delete_post'),
    path("detail/<int:id>", DetailPostView.as_view(), name='detail_post')
]
