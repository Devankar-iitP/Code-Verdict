from django.shortcuts import render, redirect
from django.contrib import messages
from Authentication.models import detail
from .decorators import unauthenticated_user
from Problem.models import question

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.info(request,'You are not logged-in ! Please log-in first to avail benefits !')
        return render(request, 'dynamic_files/prev_home.html', {'title' : 'Code Verdict'})
    
    user1 = detail.objects.get(username=request.user.username)
    messages.success(request,f'Welcome {user1.name}, your have successfully logged-in ! Happy Coding !')
    return redirect('/home')

@unauthenticated_user
def home(request):
    user1 = detail.objects.get(username=request.user.username)
    dict = {
        'title' : 'Home Page',
        'gender' : user1.gender,
        'name' : user1.name,
    }
   
    return render(request, 'dynamic_files/home.html', dict)

@unauthenticated_user
def dash(request):
    all_ques = question.objects.all()
    dict = {
        'title' : 'Dashboard',
        'all_ques' : all_ques,
    }

    return render(request,'dynamic_files/dash.html', dict)

@unauthenticated_user
def ques(request, ques_id):
    ques = question.objects.get(pk=ques_id)
    return render(request,'dynamic_files/main.html', {'title' : ques.name,'ques' : ques})