from django.contrib import admin
from .models import Main

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Main.objects.exists()