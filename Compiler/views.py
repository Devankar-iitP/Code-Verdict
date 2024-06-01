from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from Code_Verdict.decorators import unauthenticated_user
from Authentication.models import detail
from Problem.models import question, testcase
from django.conf import settings
import os, subprocess, uuid
from .models import info
from django.utils import timezone

# Create your views here.
@unauthenticated_user
def main(request, ques_id, username):
    ques = question.objects.get(pk = ques_id)
    user = User.objects.get(username=username)
    code = request.POST['code']
    language = request.POST['language']

    if len(code) < 1:
        messages.warning(request, 'Code cannot be empty !')
        return redirect(f'/dash/{ques_id}')

    if info.objects.filter(code=code, user=user, question=ques).exists():
        messages.warning(request, 'This code has already been submitted previously !')
        return redirect(f'/dash/{ques_id}')
    
    status = run(request, ques_id, code, language)
    if status == 0:
        return redirect(f'/dash/{ques_id}')

    naruto = info(user=user, question=ques, code=code, status=status, language=language,time=timezone.now())
    naruto.save()
    
    if status == 2:
        return redirect(f'/dash/{ques_id}')

    brief = detail.objects.get(username = username)
    data = info.objects.filter(user = user).order_by('-time')
    dict = {
        'title' : 'Profile',
        'user' : brief,
        'info' : data        
    }

    messages.success(request, f'Great {user.username} ! You solved it, practice more ^_^')
    return render(request, 'dynamic_files/profile.html', dict)    


def run(request, ques_id, code, language):
    ques = question.objects.get(pk = ques_id)

# ******************* Creating needed files *********************************
    testcases = testcase.objects.filter(question = ques)
    path = settings.BASE_DIR
    files = ["codes", "inputs", "outputs"]
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
    output_path = path / "outputs"/ f'{unique}.txt'
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
    elif language == '3':
        compile_result = subprocess.run(
            ["javac", code_path],
            text = True,
            capture_output=True
        )

    if language!='2' and compile_result.returncode:
        messages.warning(request, 'Compilation ERROR !')
        messages.warning(request, f'{compile_result.stderr}')
        return 0

    if language!='2' and 'run' in request.POST:
        messages.success(request, f'Compiled SUCCESSFULLY {request.user.username} ^_^')
        return 0
    
# ******************* End of Compiling Code *********************************
    
# ******************* Run CODE *********************************
    
    cnt = 1
    
# Running each testcase one-by-one and judging its correctness 
    for each_testcase in testcases:
        with open(input_path, "w") as input_file:
            input_file.write(each_testcase.inputs)

# NOTE => stdin will not work in non-interactive environment
# so you can't write and take input at the same time --> split
        with open(input_path, "r") as input_file:
            if language == '1' or language == '4':
                    run_result = subprocess.run(
                        [executable_path],
                        stdin=input_file,
                        text = True,
                        capture_output=True
                    )
            elif language == '3':
                java_class, ext = os.path.splitext(code_path)
                run_result = subprocess.run(
                    ["java", java_class],
                    stdin = input_file, 
                    capture_output=True,
                    text = True
                )
            else:
                run_result = subprocess.run(
                    ["python", code_path],
                    stdin=input_file,
                    text = True,
                    capture_output=True
                )
        
        if run_result.returncode:
            messages.warning(request, 'Compilation ERROR !')
            messages.warning(request, f'{run_result.stderr}')
            return 0
        
        if 'run' in request.POST:
            messages.success(request, f'Compiled SUCCESSFULLY {request.user.username} ^_^')
            return 0
        
# ******************* End of Run CODE *********************************

# ******************* Testing Correctness of CODE *********************************

        with open(output_path, "w") as output_file:
            output_file.write(run_result.stdout)

# Will ignore the '\n' at end
        with open(output_path, "r") as output_file:
            kakashi = output_file.read().splitlines()

# Taking care of by-mistake enter pressed by problem-setter
        minato = [s for s in each_testcase.outputs.split('\r\n') if s]

        print(minato)
        print(kakashi)
        if len(minato) != len(kakashi):
            messages.warning(request, 'Output generated must have same format as described !')
            return 0

        for tmp in range(len(minato)):
            kakashi[tmp] = kakashi[tmp].strip() 
            minato[tmp] = minato[tmp].strip() 
            if kakashi[tmp] != minato[tmp]:
                messages.warning(request, f'Wrong answer at Testcase - {cnt} !')
                messages.warning(request, f'Expected : {minato[tmp]} but Found : {kakashi[tmp]}')            
                return 2
        cnt += 1
    
    return 1

# ******************* End of Testing Correctness of CODE *********************************