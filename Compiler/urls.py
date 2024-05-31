from django.urls import path
from . import views

urlpatterns = [
    path("<int:ques_id>/<str:username>/", views.main),
]
