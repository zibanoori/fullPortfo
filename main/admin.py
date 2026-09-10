from django.contrib import admin
from .models import Main, Project

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Main.objects.exists()
    
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'tags']
    search_fields = ['title', 'description']    