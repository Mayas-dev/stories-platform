from django.contrib import admin

# Register your models here.

from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'genre', 'status', 'created_at')
    list_filter = ('status', 'genre', 'audience')
    search_fields = ('name', 'content')