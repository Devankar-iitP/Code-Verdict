from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import detail

# Create your views here.
# username = request.POST['username'] same as username = request.POST.get('username')

def reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        gender = request.POST['Gender']
        num = request.POST['number']        
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['re-password']
        role = request.POST['Role']

# ***************** Handling error messages ****************************
        if (len(username) < 4 or len(name) < 4):
            messages.warning(request, 'Name or username cannot be less than 4 characters  !')
            return redirect("/auth/registration/")
        
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Someone with the same username already exists !')
            return redirect("/auth/registration/")

        if pass1!=pass2:
            messages.warning(request,'Password does not match with Confirm Password. Try again !')
            return redirect("/auth/registration/")
        
        if len(pass1) < 5:
            messages.warning(request,'Password length cannot be less than 5 characters !')
            return redirect("/auth/registration/")
        
        if len(num) != 10:
            messages.warning(request,'Contact number must consists of exactly 10 digits. Try again !')
            return redirect("/auth/registration/")
        
        if username.isspace():
            messages.warning(request,'Username cannot contain spacing characters !')
            return redirect("/auth/registration/")
# ***************** End of handling error messages ****************************

# ***************** Creating user with above details ****************************

        user = detail(name= name ,mail= mail ,num= num , gender= gender ,username= username, approved = 0)
        user1 = User.objects._create_user(username, mail, pass1)
        user1.set_password(pass1)
        user.save()
        user1.save()
        
        messages.success(request,f'Welcome {name}, your account is created successfully ^_^')
        if role == '1':
            grp = Group.objects.get(name='Student')
        else:
            messages.warning(request,'NOTE - You will be authorized as employee only after verification from admin !!')
            grp = Group.objects.get(name='Employee')

        user1.groups.add(grp)
# ***************** End of creating user with above details ****************************

        return redirect('/auth/login/')
    
    return render(request, 'dynamic_files/registration.html', {'title' : 'Registration Page'})

def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            messages.warning(request,'You don\'t have an account. Please create one !')
            return redirect("/auth/registration/")
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request,'Invalid password ! Try again !')
            return redirect('/auth/login')

        login(request,user)
        user1 = detail.objects.get(username=request.user.username)
        messages.success(request,f'Welcome {user1.name}, your have successfully logged-in ! Happy Coding !')
        return redirect('/home')

    return render(request, 'dynamic_files/login.html', {'title' : 'Login Page'})

def log_out(request):
    messages.warning(request,'You have been successfully logged-out ! Hope to see you again :-)')
    logout(request)
    return redirect('/')