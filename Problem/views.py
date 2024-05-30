from django.shortcuts import render, redirect
from django.contrib import messages
from Code_Verdict.decorators import allowed_users
from .models import question, testcase

# Create your views here.
@allowed_users(allowed_roles=['Employee'])
def ques(request):
    if request.method == 'POST':
        name = request.POST['name']
        difficulty = request.POST['difficulty']
        description = request.POST['desc']
        in_format = request.POST['in_format']
        out_format = request.POST['out_format']
        type_name = request.POST['type_name']

        if len(name) < 1 :
            messages.warning(request, 'Problem name cannot be empty !')
            return redirect("/ques")

        if len(description) < 10 :
            messages.warning(request, 'Description cannot be less than 10 characters !')
            return redirect("/ques")
        
        if len(in_format) < 10 :
            messages.warning(request, 'Input Format cannot be less than 10 characters !')
            return redirect("/ques")
        
        if len(out_format) < 10 :
            messages.warning(request, 'Output Format cannot be less than 10 characters !')
            return redirect("/ques")
        
        if question.objects.filter(name=name).exists():
            messages.warning(request,'Some Problem with the same name already exists !')
            return redirect("/ques")
        
        user = question(name= name ,difficulty= difficulty ,description= description, in_format= in_format, out_format= out_format, type_name = type_name)
        user.save()

        dict={
            'title' : 'Create Testcase',
            'chk' : 1,
            'id_' : name,
        }

        if 'test' in request.POST:
            messages.success(request,'Congratulations ! You have created a problem successfully ^_^')
            return render(request, 'dynamic_files/testcase_set.html', dict)
        else:
            messages.success(request,'Congratulations ! You have created a problem successfully ^_^')
            return redirect('/ques')

    return render(request,'dynamic_files/question_set.html', {'title' : 'Create Question'})

@allowed_users(allowed_roles=['Employee'])
def test(request):
    if request.method == 'POST':
        in_format = request.POST['inputs']
        out_format = request.POST['outputs']
        name = request.POST['name']
        id_ = request.POST['id_']

        dict1 ={
            'title' : 'Create Testcase',
            'chk' : 1,
            'id_' : id_
        }

        if len(in_format) < 1 :
            messages.warning(request, 'Input cannot be empty !')
            if id_ != '-1':
                return render(request, 'dynamic_files/testcase_set.html', dict1)
            return redirect("/ques/test")
        
        if len(out_format) < 1 :
            messages.warning(request, 'Output cannot be empty !')
            if id_ != '-1':
                return render(request, 'dynamic_files/testcase_set.html', dict1)
            return redirect("/ques/test")
        
        if id_ == '-1' and len(name) < 1:
            messages.warning(request, 'Problem cannot be empty !')
            return redirect("/ques/test")
        
        if name != '-1':
            id_ = name

        try:
            ques = question.objects.get(name = id_)
        except question.DoesNotExist:
            messages.warning(request,'Problem Name is case-sensitive, please enter again !')
            return redirect('/ques/test')        

        if testcase.objects.filter(question = ques, inputs=in_format, outputs=out_format).exists():
            messages.warning(request,'Testcase already exists !')
            if id_ != '-1':
                return render(request, 'dynamic_files/testcase_set.html', dict1)
            return redirect("/ques/test")
        
        user = testcase(question = ques, inputs= in_format, outputs= out_format)
        user.save()

        dict1['id_'] = id_
        
        if 'test' in request.POST:
            messages.success(request,'Congratulations ! You have added testcase successfully ^_^')
            return render(request, 'dynamic_files/testcase_set.html', dict1)
        else:
            messages.success(request,'Congratulations ! You have added testcase successfully ^_^')
            return redirect('/dash')

    dict={
        'title' : 'Create Testcase',
        'chk' : 0,
    }
    return render(request,'dynamic_files/testcase_set.html', dict)