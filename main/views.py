from django.shortcuts import render
from .models import Main, Project


def index(request):
    main_details = Main.objects.first()
    projects = Project.objects.all()
    
    for proj in projects:
        if proj.tags:
            proj.tag_list = [tag.strip() for tag in proj.tags.split(',')]
        else:
            proj.tag_list = []

    context = {
        "details": main_details,
        "projects": projects
    }
    
    return render(request, "index.html", context=context)