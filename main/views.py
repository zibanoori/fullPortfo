from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Main, Project, Skill, ContactMessage


def index(request):
    main_details = Main.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    
    for proj in projects:
        if proj.tags:
            proj.tag_list = [tag.strip() for tag in proj.tags.split(',')]
        else:
            proj.tag_list = []

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Thank you! Your message has been sent.")
            return redirect('index') 

    context = {
        "details": main_details,
        "projects": projects,
        "skills": skills
    }
    
    return render(request, "index.html", context=context)