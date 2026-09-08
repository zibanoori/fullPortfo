from django.shortcuts import render


def index(request):
    main_details = Main.objects.first()
    
    context = {
        "details" : main_details
    }
    
    return render(request,"index.html", context=context) 