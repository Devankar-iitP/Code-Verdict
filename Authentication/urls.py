from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.reg),
    path("login/", views.log),
    path("logout/", views.log_out),
]
