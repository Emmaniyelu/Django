from django.shortcuts import render
from app1.models import emp 
# Create your views here.
def display_emp(request):
    qs=emp.objects.all()
    response=render(request,"app1/display.html",context={'qs':qs})
    return response


def view_emp(request):
    j=request.GET['job']
    if j!='all':
        qs=emp.objects.filter(job=j)
    else:
        qs=emp.objects.all()


    response=render(request,"app1/show_emp.html",context={"qs":qs})
    
    return response 


def display_empjob(request):
    response=render(request,"app1/view_emp.html")
    return response 
