from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Activity,Project
from django.contrib import messages
# Create your views here.


@login_required(login_url='/authentication/login')
def index(request):
    projects=Project.objects.filter(owner=request.user)
    activity=Activity.objects.filter(owner=request.user)
    context={
        'activity':activity,
        'projects':projects,
    }
    return render(request,'activity/index.html',context)

def add_activity(request):
    projects=Project.objects.filter(owner=request.user)
    context={
        'projects':projects,
    }
    if request.method=='GET':
        return render(request,'activity/add_activity.html',context)

    if request.method=='POST':
        date=request.POST.get('date',False)
        if not date:
            messages.error(request,'Input date!')
            return render(request,'activity/add_activity.html')
        
        sleep=request.POST.get('sleep',False)
        if not sleep:
            messages.error(request,'Input Duration of Sleep!')
            return render(request,'activity/add_activity.html')
        
        qsleep=request.POST.get('qsleep',False)
        if not qsleep:
            messages.error(request,'Input Quality of Sleep!')
            return render(request,'activity/add_activity.html')
        
        
        classes=request.POST.get('classes',False)
        if not classes:
            messages.error(request,'Input Number of Classes!')
            return render(request,'activity/add_activity.html')
        
        workout=request.POST.get('workout',False)
        if not workout:
            messages.error(request,'Input Hours of Workout!')
            return render(request,'activity/add_activity.html')
        
        qday=request.POST.get('qday',False)
        if not qday:
            messages.error(request,'Input Quality of Day!')
            return render(request,'activity/add_activity.html')

        pname=request.POST.get('pname',False)
        if not pname:
            pname='None'

        phours=request.POST.get('phours',False)
        if not phours:
            messages.error(request,'Input Quality of Day!')
            return render(request,'activity/edit_activity.html',context)

        if Activity.objects.filter(owner=request.user,date=date).exists():
            messages.error(request,'Record of the same date already exists!')
            return render(request,'activity/add_activity.html')

        if (int(sleep)<0 or int(sleep) >24):
            messages.error(request,'Sleep should be within 24 hours!')
            return render(request,'activity/add_activity.html')

        Activity.objects.create(owner=request.user,date=date,sleep=sleep,qsleep=qsleep,classes=classes,workout=workout,qday=qday,project=pname,phours=phours)
        messages.success(request,'Activity saved successfully!')
        return redirect('activity')

def activity_edit(request,id):
    activity = Activity.objects.get(pk=id)
    context={
        'activity':activity
    }
    if request.method=='GET':
        
        return render(request,'activity/edit_activity.html',context)

    if request.method=='POST':

        date=request.POST.get('date',False)
        if not date:
            messages.error(request,'Input date!')
            return render(request,'activity/edit_activity.html',context)
        
        sleep=request.POST.get('sleep',False)
        if not sleep:
            messages.error(request,'Input Duration of Sleep!')
            return render(request,'activity/edit_activity.html',context)
        
        qsleep=request.POST.get('qsleep',False)
        if not qsleep:
            messages.error(request,'Input Quality of Sleep!')
            return render(request,'activity/edit_activity.html',context)
        
        
        classes=request.POST.get('classes',False)
        if not classes:
            messages.error(request,'Input Number of Classes!')
            return render(request,'activity/edit_activity.html',context)
        
        workout=request.POST.get('workout',False)
        if not workout:
            messages.error(request,'Input Hours of Workout!')
            return render(request,'activity/edit_activity.html',context)
        
        qday=request.POST.get('qday',False)
        if not qday:
            messages.error(request,'Input Quality of Day!')
            return render(request,'activity/edit_activity.html',context)

        pname=request.POST.get('pname',False)
        if not pname:
            pname='None'
            
        phours=request.POST.get('phours',False)
        if not phours:
            messages.error(request,'Input Quality of Day!')
            return render(request,'activity/edit_activity.html',context)

        # if Activity.objects.filter(owner=request.user,date=date).exists():
        #     messages.error(request,'Record of the same date already exists!')
        #     return render(request,'activity/edit_activity.html',context)

        if (int(sleep)<0 or int(sleep) >24):
            messages.error(request,'Sleep should be within 24 hours!')
            return render(request,'activity/edit_activity.html',context)

       
        activity.owner=request.user
        activity.date=date
        activity.sleep= sleep
        activity.qsleep=qsleep
        activity.classes=classes
        activity.workout=workout
        activity.qday=qday
        activity.phours=phours
        activity.save()
        return redirect('activity')
        
def delete_activity(request,id):
    activity=Activity.objects.get(pk=id)
    activity.delete()
    messages.success(request,'Activity Deleted.')
    return redirect('activity')

def projects(request):
    project=Project.objects.filter(owner=request.user)
    context={
        'project':project
    }
    return render(request,'activity/projects.html',context)

def add_project(request):
    if request.method=='GET':
        return render(request,'activity/add_project.html')
    
    if request.method=='POST':
        pname=request.POST.get('pname',False)
        if not pname:
            messages.error(request,'Input a project name!')
            return render(request,'activity/add_project.html')

        pdesc=request.POST.get('pdesc',False)
        if not pdesc:
            messages.error(request,'Input a project description!')
            return render(request,'activity/add_project.html')

        Project.objects.create(name=pname,owner=request.user,details=pdesc)
        messages.success(request,'Project added successfully!')
        return redirect('projects')

def project_edit(request,id):
    project=Project.objects.get(pk=id)
    context={
        'project':project
    }
    if request.method=='GET':
        return render(request,'activity/edit_project.html',context)
    
    if request.method=='POST':
        pname=request.POST.get('pname',False)
        if not pname:
            messages.error(request,'Input a project name!')
            return render(request,'activity/edit_project.html',context)

        pdesc=request.POST.get('pdesc',False)
        if not pdesc:
            messages.error(request,'Input a project description!')
            return render(request,'activity/edit_project.html',context)

        project.owner=request.user
        project.name=pname
        project.details=pdesc
        project.save()
        messages.success(request,'Project edited successfully!')
        return redirect('projects')