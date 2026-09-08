from django.db import models

class main(models.Model):
    logo = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=100, blank=True)
    github_url = models.URLField(max_length=250, blank=True)
    linkedin_url = models.URLField(max_length=250, blank=True)
    copyright = models.CharField(max_length=200, blank=True)
    made_with = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)