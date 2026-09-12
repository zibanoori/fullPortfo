from django.db import models

class Main(models.Model):
    class Meta:
        verbose_name_plural = "Main Details"
        
    favicon = models.ImageField(upload_to='main/', blank=True, null=True) 
    title = models.CharField(max_length=75, blank=True, help_text="This is a text. Not an image.")
    description = models.TextField(blank=True)
    logo = models.CharField(max_length=50, blank=True, help_text="This is a text. Not an image.")
    github_url = models.URLField(max_length=250, blank=True)
    linkedin_url = models.URLField(max_length=250, blank=True)
    copyright = models.CharField(max_length=200, blank=True)
    made_with = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    footer_description = models.TextField(blank=True)
    def __str__(self):
        return "Main Details"
    
    
class Project(models.Model):
    
    title = models.CharField(max_length=150, blank=True, verbose_name="Project Title")
    featured_image = models.ImageField(upload_to="projects/")
    description = models.TextField(blank=True)
    view_projects_link = models.URLField(blank=True)
    view_code_link = models.URLField(blank=True)
    tags = models.CharField(max_length=150, blank=True)
    
    class Meta:
        verbose_name_plural = "Projects"
        
    def __str__(self):
        return self.title
    
    
class Skill(models.Model):
    class Meta:
        verbose_name="Skill"
        verbose_name_plural = "Skills"
        
    name = models.CharField(max_length=150, blank=True)
    icons = models.CharField(max_length=100, blank=True)
    skills_title = models.CharField(max_length=100, blank=True, default="I Work With")
    skills_description = models.TextField(blank=True, default="Building skills in")
    def __str__(self):
        return self.name