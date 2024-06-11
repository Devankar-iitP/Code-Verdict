from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from Authentication.models import detail
from .decorators import unauthenticated_user
from Problem.models import question, testcase
from Compiler.models import info
import os, subprocess, uuid
from django.conf import settings

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
    try:
        test = testcase.objects.filter(question = ques)[0]
    except:
        messages.warning(request, 'First create a test-case !!')
        return redirect('/ques/test')

    dict = {
        'title' : ques.name,
        'ques' : ques,
        'test' : test
    }
    return render(request,'dynamic_files/main.html', dict)

@unauthenticated_user
def profile(request):
    user = User.objects.get(username=request.user.username)
    brief = detail.objects.get(username = request.user.username)
    data = info.objects.filter(user = user).order_by('-time')

    a = b = c = d = streak = tmp = 0
    for submission in data:
        if submission.status == 1:
            tmp += 1
        else:
            streak = max(streak, tmp)
            tmp=0

        if submission.language == '1':
            a+=1
        elif submission.language == '2':
            b+=1
        elif submission.language == '3':
            c+=1
        else:
            d+=1
    streak = max(streak, tmp)

    dict = {
        'title' : 'Profile',
        'user' : brief,
        'info' : data,
        'cpp' : (a/(a+b+c+d))*100 if a+b+c+d != 0 else 0,
        'py' : (b/(a+b+c+d))*100 if a+b+c+d != 0 else 0,
        'java' : (c/(a+b+c+d))*100 if a+b+c+d != 0 else 0,
        'c' : (d/(a+b+c+d))*100 if a+b+c+d != 0 else 0,
        'streak' : streak
    }
    return render(request,'dynamic_files/profile.html', dict)

@unauthenticated_user
def custom(request):
    if request.method == 'POST':
        code = request.POST['code']
        language = request.POST['language']
        input_data = request.POST['inputs']

        if len(code) < 1:
            messages.warning(request, 'Code cannot be empty !')
            return redirect('/custom')
        
# ******************* Creating needed files *********************************
        path = settings.BASE_DIR
        files = ["codes", "inputs"]
        for file in files:
            os.makedirs(path/file, exist_ok = True)

        # uuid version 4 generates unique O/P everytime and more secure than uuid1
        unique = str(uuid.uuid4())
        dict = {
            '1' : 'c++',
            '2' : 'py',
            '3' : 'java',
            '4' : 'c'
        }

        dict1 ={
            '1' : 'g++',
            '4' : 'gcc'
        }

        code_path = path / "codes"/ f'{unique}.{dict[language]}'
        input_path = path / "inputs"/ f'{unique}.txt'

    # newline maintains the exact code and don't cause extra whitespaces
        with open(code_path, "w", newline='\n') as code_file:
            code_file.write(code)  

# ******************* End of Creating needed files *********************************

# ******************* Compiling Code *********************************

        if language == '1' or language == '4':
            executable_path = path / "codes" / unique
# similar to [ g++ file_name.cpp -o name ] running in cmd
# -o renames the executable file (like ./a.out) jb run krte the labs mai
            compile_result = subprocess.run(
                [dict1[language], code_path, "-o", executable_path],
                capture_output= True,
                text = True
            )

            if compile_result.returncode:
                messages.warning(request, 'Compilation ERROR !')
                messages.warning(request, f'{compile_result.stderr}')
                return redirect('/custom')
    
# ******************* End of Compiling Code *********************************
    
# ******************* Run CODE *********************************
    
        with open(input_path, "w") as input_file:
            input_file.write(input_data)

# NOTE => stdin will not work in non-interactive environment
# so you can't write and take input at the same time --> split
        with open(input_path, "r") as input_file:
            try:
                if language == '1' or language == '4':
                        run_result = subprocess.run(
                            [executable_path],
                            stdin=input_file,
                            text = True,
                            capture_output=True,
                            timeout=2
                        )
                elif language == '3':
                    run_result = subprocess.run(
                        ["java", code_path],
                        stdin = input_file, 
                        capture_output=True,
                        timeout=2,
                        text = True
                    )
                else:
                    run_result = subprocess.run(
                        ["python3", code_path],
                        stdin=input_file,
                        text = True,
                        capture_output=True,
                        timeout=2
                    )
            except subprocess.TimeoutExpired:
                # Check if the subprocess is still running after 2 seconds
                messages.warning(request, 'ERROR : TLE ! Time limit of 2 seconds !! ')
                return redirect('/custom')
        
        if run_result.returncode:
            messages.warning(request, 'Compilation ERROR !')
            messages.warning(request, f'{run_result.stderr}')
            return redirect('/custom')
        
# ******************* End of Run CODE *********************************

        dict3 = {
            'outputs' : run_result.stdout,
            'inputs' : input_data,
            'code' : code,
            'lang' : language,
            'chk' : 1
        }
    
        messages.success(request, f'Compiled SUCCESSFULLY {request.user.username} ^_^')
        return render(request,'dynamic_files/custom.html', dict3)
    
    return render(request,'dynamic_files/custom.html', {'title' : 'Custom Input', 'chk' : 0})