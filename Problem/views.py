from django.shortcuts import render, redirect
from django.contrib import messages
from Code_Verdict.decorators import allowed_users
from .models import question, testcase, attempt

# Create your views here.
@allowed_users(allowed_roles=['Employee'])
def ques(request):
    if request.method == 'POST':
        name = request.POST['name']
        difficulty = request.POST['difficulty']
        description = request.POST['desc']
        in_format = request.POST['in_format']
        out_format = request.POST['out_format']

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
        
        user = question(name= name ,difficulty= difficulty ,description= description, in_format= in_format, out_format= out_format)
        user.save()

        messages.success(request,'Congratulations ! You have created a problem successfully ^_^')
        return redirect('/ques')

    return render(request,'dynamic_files/question_set.html', {'title' : 'Create Question'})

@allowed_users(allowed_roles=['Employee'])
def test(request):
    if request.method == 'POST':
        question = request.POST['name']
        in_format = request.POST['in_format']
        out_format = request.POST['out_format']

        if len(in_format) < 10 :
            messages.warning(request, 'Input Format cannot be less than 10 characters !')
            return redirect("/ques")
        
        if len(out_format) < 10 :
            messages.warning(request, 'Output Format cannot be less than 10 characters !')
            return redirect("/ques")
        
        # user = question(name= name ,difficulty= difficulty ,description= description, in_format= in_format, out_format= out_format)
        # user.save()

        messages.success(request,'Congratulations ! You have created a problem successfully ^_^')
        return redirect('/ques')

    return render(request,'dynamic_files/testcase_set.html', {'title' : 'Create Testcase'})