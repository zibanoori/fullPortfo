from django.shortcuts import render
from .models import Main


def index(request):
    main_details = Main.objects.first()
    
    context = {
        "details" : main_details
    }
    
    return render(request,"index.html", context=context) 