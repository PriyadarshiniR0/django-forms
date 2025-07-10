from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_dept(request):
    if request.method=='POST':
        Dno=request.POST['Dno']
        DTO=dept.objects.get_or_create(Dno=Dno)
        if DTO[1]:
            return HttpResponse(f'{Dno} object is created')
        else:
            return HttpResponse(f'{Dno} is already exist')
    return render(request,'insert_dept.html')

def insert_emp(request):
    DTO=dept.objects.all()
    Mg=emp.objects.all()
    d={'DTO':DTO,'Mg':Mg}

    if request.method=='POST':

        Eno=request.POST['Eno']
        Ename=request.POST['Ename']
        job = request.POST['job']
        sal = request.POST['sal']
        comm = request.POST['comm']
        Hiredate = request.POST['Hiredate']
        Dno=request.POST['Dno']
        Mgr= request.POST['Mgr']

        DO=dept.objects.get(Dno=Dno)
        Mgo=emp.objects.get(Eno=Mgr)
        
        ETO=emp.objects.get_or_create(Eno=Eno,Ename=Ename, job=job,sal=sal,comm=comm,Hiredate=Hiredate,Dno=DO,Mgr=Mgo)
        if ETO[1]:
            return HttpResponse('emp is created')
        else:
            return HttpResponse('emp is already present ')
               
    return render(request,'insert_emp.html',d)
    