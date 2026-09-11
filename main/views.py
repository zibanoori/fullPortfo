from django.shortcuts import render
from .models import Main, Project


def index(request):
    main_details = Main.objects.first()
    projects = Project.objects.all()
    
    context = {
        "details" : main_details,
        "projects" : projects
    }
    
    return render(request,"index.html", context=context) 