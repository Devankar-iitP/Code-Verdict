from django.shortcuts import render,redirect
from django.contrib import messages

def unauthenticated_user(view_func):
    def zoro(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "You cannot access this page ! Please log-in first to avail benefits !")
            return render(request, 'dynamic_files/prev_home.html', {'title' : 'Code Verdict'})
        
        return view_func(request, *args, **kwargs)
    
    return zoro

def allowed_users(allowed_roles = []):
    def nami(view_func):
        def sanji(request, *args, **kwargs):
            if request.user.groups.exists():

# For the time being considering that one user belongs to one group only
                grp = request.user.groups.all()[0].name
                if grp in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    messages.info(request, "You cannot access this page ! You are not an Employee !")
                    return redirect('/home')

            messages.info(request, "You cannot access this page ! Please log-in first to avail benefits !")
            return render(request, 'dynamic_files/prev_home.html', {'title' : 'Code Verdict'})
        
        return sanji
    return nami