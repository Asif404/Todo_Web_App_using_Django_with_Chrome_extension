from django.http.response import HttpResponseBadRequest
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib.auth import login,logout
from .forms import *
from django.http import JsonResponse
# Create your views here.
def home(request):
    task=Task.objects.all()
    title=TodoTitile.objects.all()
    titleform=AddTitle()
    taskform=AddTask()
    taskcompleted=Task.objects.filter(complete=True).count
    taskinprogress=Task.objects.filter(complete=False).count
    if 'create_title' in request.POST:
        titleform=AddTitle(request.POST)
        if titleform.is_valid():
            titleform.save()
        return redirect('/')
    elif 'create_task' in request.POST:
        taskform=AddTask(request.POST)
        if taskform.is_valid():
            taskform.save()
        return redirect('/')
        
    context={'task':task,'title':title,'titleform':titleform,'taskform':taskform,'taskcompleted':taskcompleted,'taskinprogress':taskinprogress}
    return render(request, 'polls/index.html',context)

def post_form_api(request):
    data={}
    if request.method == "POST":
        taskid = request.POST['taskid']
        status = request.POST['status']
        task = Task.objects.get(pk=taskid)
        if status == 'True':
            task.complete = True
            data['result']=True
        else:
            task.complete = False
            data['result']=True
        task.save()
        if request.is_ajax():
            return JsonResponse(data)
        else:
            return HttpResponseBadRequest()
    
def del_task(request):
    data={}
    if request.method=="POST":
        taskid=request.POST['taskid']
        task=Task.objects.get(pk=taskid)
        task.delete()
        data['result']=True
        if request.is_ajax():
            return JsonResponse(data)
        else:
            return HttpResponseBadRequest()
def del_titile(request):
    data={}
    if request.method=="POST":
        titleid=request.POST['titleid']
        title=TodoTitile.objects.get(pk=titleid)
        print(title)
        title.delete()
        data['result']=True
        if request.is_ajax():
            return JsonResponse(data)
        else:
            return HttpResponseBadRequest()
        