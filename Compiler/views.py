from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'dynamic_files/result.html')