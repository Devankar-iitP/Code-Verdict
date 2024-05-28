from django.urls import path
from . import views

urlpatterns = [
    path('', views.ques),
    path('test/', views.test),
]