from django.urls import path
from . import views

urlpatterns = [
    path('', views.ques),
    path('test/', views.test),
    path('update/<int:ques_id>/', views.update),
    path('delete/<int:ques_id>/', views.delete),
]