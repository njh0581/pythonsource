from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = "blog"

urlpatterns = [
    # http://localhost:8000/blog/
    path("", views.list, name="list"),
    # http://localhost:8000/blog/post/1
    path("post/<int:post_id>/", views.detail, name="detail"),
    # http://localhost:8000/blog/post/create
    path("post/create/", views.create, name="create"),
    # http://localhost:8000/blog/post/modify/1
    path("post/modify/<int:post_id>/", views.modify, name="modify"),
    # http://localhost:8000/blog/post/delete/1
    path("post/delete/<int:post_id>/", views.delete, name="delete"),
]
