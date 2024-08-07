from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.common_login, name="login"),
    path("logout/", views.common_logout, name="logout"),
]
