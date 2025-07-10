from django.shortcuts import render

from app.models import *

from app.forms import *

from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tname=TFDO.cleaned_data['tname']
            LTO=Topic.objects.get_or_create(tname=tname)
            if LTO[1]:
             return HttpResponse('New Topic is created')
            else:
                return HttpResponse('Topic is already present')
        else:
            return HttpResponse('Invalid data')

    
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tname=WFDO.cleaned_data['tname']
            name=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']
            email=WFDO.cleaned_data['email']
            TO=Topic.objects.get(tname=tname)
            WTO=Webpage.objects.get_or_create(tname=TO,name=name,url=url,email=email)
            if WTO[1]:
                return HttpResponse('Name is created')
            else:
                return HttpResponse('name is already present') 
    
    return render (request,'insert_webpage.html',d)