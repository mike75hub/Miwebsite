from django.shortcuts import render
from .models import Project, SocialLink, WorkExperience

def home(request):
    # Get featured projects first, then others, ordered by display order
    projects = Project.objects.all().order_by('-display_order', '-created_at')
    
    # Get active social links ordered by display order
    social_links = SocialLink.objects.filter(is_active=True).order_by('-display_order')
    
    # Get work experience ordered by display order
    work_experience = WorkExperience.objects.all().order_by('-display_order', '-start_date')
    context = {
        'projects': projects,
        'social_links': social_links,
        'work_experience': work_experience,
        'profile': {
            'name': 'SanviHome',
            'title': 'I am a software developer',  # Update this with your title
            'bio': 'Passionate developer creating amazing digital experiences and solving complex problems through code. I love bringing ideas to life with modern technologies.But i am still figuring things out',  # Update this
        }
    }
    return render(request, 'portfolio/home.html', context)