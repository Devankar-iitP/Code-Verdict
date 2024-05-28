from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.req),
    path("login/", views.log),
    path("logout/", views.log_out),
]
