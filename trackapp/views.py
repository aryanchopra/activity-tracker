from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Activity,Project
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User



def search_activity(request):
    if request.method=='POST':
        search_str=json.loads(request.body).get('searchText')
        activity= Activity.objects.filter(owner=request.user, date__istartswith=search_str) | Activity.objects.filter(owner=request.user, project__istartswith=search_str) | Activity.objects.filter(owner=request.user, qsleep__istartswith=search_str)

        data=activity.values()
        return JsonResponse(list(data),safe=False)

@login_required(login_url='/authentication/login')
def index(request):
    projects=Project.objects.filter(owner=request.user)
    activity=Activity.objects.filter(owner=request.user)
    paginator = Paginator(activity,5) #number of activities per page
    page_number = request.GET.get('page')
    page_obj=Paginator.get_page(paginator, page_number)
    context={
        'activity':activity,
        'projects':projects,
        'page_obj':page_obj,
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

def sleepstatistics(request):
    return render(request,'activity/sleepstatistics.html')

def projectstatistics(request):
    return render(request,'activity/projectstats.html')

def workoutstatistics(request):
    return render(request,'activity/summarystats.html')
    
def daystatistics(request):
    return render(request,'activity/daystats.html')

def get_data(request):
    todays_date=datetime.date.today()
    one_month_ago= todays_date-datetime.timedelta(days=30)
    activities=Activity.objects.filter(owner=request.user,date__gte=one_month_ago,date__lte=todays_date)

    sleepdict={}
    qsleepdict={}
    projectdict={}
    workoutdict={}
    qdaydict={}
    classesdict={}

    class Getdata:

        

        def get_sleep(activity):
            date= str(activity.date)
            sleep= activity.sleep
            return {date:sleep}

        def get_qsleep(activity):
            date= str(activity.date)
            qsleep= activity.qsleep
            return {date:qsleep}

        def get_project(activity):
            return activity.project

        def get_workout(activity):
            date= str(activity.date)
            workout= activity.workout
            return {date:workout}

        def get_qday(activity):
            date= str(activity.date)
            qday= activity.qday
            return {date:qday}

        def get_classes(activity):
            date= str(activity.date)
            classes= activity.classes
            return {date:classes}
        

        def get_project_hours(project):
            hours=0
            for x in activities.filter(project=project):
                hours+=x.phours

            return hours

        def get_monthly_project_hours():
            hours=0
            for x in activities:
                hours+=x.phours
            return hours

        def get_monthly_class_hours():
            hours=0
            for x in activities:
                hours+=x.classes
            return hours

        def get_monthly_workout_hours():
            hours=0
            for x in activities:
                hours+=x.workout
            return hours

        def get_monthly_sleep_hours():
            hours=0
            for x in activities:
                hours+=x.sleep
            return hours

    
    
    project_list=list(set(map(Getdata.get_project,activities)))
    sleep_list=list(map(Getdata.get_sleep,activities))
    qsleep_list=list(map(Getdata.get_qsleep,activities))
    workout_list=list(map(Getdata.get_workout,activities))
    qday_list=list(map(Getdata.get_qday,activities))
    classes_list=list(map(Getdata.get_classes,activities))
    tdict={'project':Getdata.get_monthly_project_hours(),'class':Getdata.get_monthly_class_hours(),'workout':Getdata.get_monthly_workout_hours(),'sleep':Getdata.get_monthly_sleep_hours()}
    
    
    
    count=0
    for x in activities:
        count+=1
    
    avg_dict={'project':round(tdict['project']/count,2), 'classes':round(tdict['class']/count),'workout':round(tdict['workout']/count),'sleep':round(tdict['sleep']/count,2)}

    for x in activities:
        for y in project_list:
            projectdict[y]=Getdata.get_project_hours(y)

    for y in sleep_list:
        for key,val in y.items():
            sleepdict[key]=val
    for y in qsleep_list:
        for key,val in y.items():
            qsleepdict[key]=val

    for y in workout_list:
        for key,val in y.items():
            workoutdict[key]=val

    for y in qday_list:
        for key,val in y.items():
            qdaydict[key]=val

    for y in classes_list:
        for key,val in y.items():
            classesdict[key]=val


    


    return JsonResponse({'averages':avg_dict,'sleep_data':sleepdict,'qsleep_data':qsleepdict,'project_data':projectdict,'workout_data':workoutdict,'qday_data':qdaydict,'classes_data':classesdict,'total':tdict}, safe=False)

             
            

# class ChartData(APIView,request):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         todays_date=datetime.date.today()
#         one_month_ago= todays_date-datetime.timedelta(days=30)
#         activities=[user.date for user in Activity.objects.all()]

#         # usernames = [user.username for user in User.objects.all()]
#         return Response(activities)