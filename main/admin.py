from django.contrib import admin
from .models import Main, Project, Skill

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Main.objects.exists()
    
    fields = [
        'title', 'logo', 'favicon', 'description',
        'github_url', 'linkedin_url', 'email', 'address',
        'about_label', 'about_title', 'about_text', 'journey_title',
        'skills_title', 'skills_description',
        'copyright', 'made_with', 'footer_description'
    ]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'tags', 'featured_image']
    search_fields = ['title', 'description']
    list_filter = ['tags'] 
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name","icons"]
    search_fields = ["name"]    