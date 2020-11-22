from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index,name="activity"),
    path('add-activity', views.add_activity,name="add-activity"),
    path('activity-edit/<int:id>', views.activity_edit,name="activity-edit"),
    path('activity-delete/<int:id>', views.delete_activity,name="activity-delete"),
    path('projects', views.projects,name="projects"),
    path('add-project', views.add_project,name="add-project"),
    path('project-edit/<int:id>', views.project_edit,name="project-edit"),
    path('search-activity', csrf_exempt(views.search_activity),name="search-activity"),
    path('sleepstatistics', views.sleepstatistics,name="sleepstatistics"),
    path('projectstatistics', views.projectstatistics,name="projectstatistics"),
    path('summarystatistics', views.workoutstatistics,name="summarystatistics"),
    path('daystatistics', views.daystatistics,name="daystatistics"),
    path('get_data',views.get_data,name='get_data')

]
