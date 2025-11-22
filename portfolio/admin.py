from django.contrib import admin
from .models import Project, SocialLink, WorkExperience

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'end_date', 'currently_working', 'display_order']
    list_filter = ['currently_working', 'start_date']
    search_fields = ['company', 'position', 'description']
    list_editable = ['display_order', 'currently_working']
    fieldsets = (
        ('Job Information', {
            'fields': ('company', 'position', 'company_url')
        }),
        ('Employment Period', {
            'fields': ('start_date', 'end_date', 'currently_working')
        }),
        ('Details', {
            'fields': ('description', 'technologies')
        }),
        ('Display Settings', {
            'fields': ('display_order',),
            'classes': ('collapse',)
        }),
    )

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'display_order', 'created_at', 'technologies']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['is_featured', 'display_order']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'technologies')
        }),
        ('Media & Links', {
            'fields': ('image', 'project_url', 'github_url')
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'display_order'),
            'classes': ('collapse',)
        }),
    )

class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'display_name', 'url', 'is_active', 'display_order']
    list_filter = ['platform', 'is_active']
    search_fields = ['platform', 'display_name', 'url']
    list_editable = ['is_active', 'display_order']
    fieldsets = (
        ('Link Information', {
            'fields': ('platform', 'url', 'display_name')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'display_order'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)