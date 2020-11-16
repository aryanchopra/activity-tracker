from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="activity"),
    path('add-activity', views.add_activity,name="add-activity"),
    path('activity-edit/<int:id>', views.activity_edit,name="activity-edit"),
    path('activity-delete/<int:id>', views.delete_activity,name="activity-delete"),
    path('projects', views.projects,name="projects"),
    path('add-project', views.add_project,name="add-project"),
    path('project-edit/<int:id>', views.project_edit,name="project-edit"),

]
