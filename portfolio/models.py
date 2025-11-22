from django.db import models

class WorkExperience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave empty if currently working here")
    currently_working = models.BooleanField(default=False)
    description = models.TextField(help_text="Describe your responsibilities and achievements")
    technologies = models.CharField(max_length=300, help_text="Technologies used (comma-separated)")
    company_url = models.URLField(blank=True, null=True)
    display_order = models.IntegerField(default=0, help_text="Higher number displays first")
    
    class Meta:
        ordering = ['-display_order', '-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    project_url = models.URLField(blank=True, null=True, verbose_name="Live Demo URL")
    github_url = models.URLField(blank=True, null=True, verbose_name="GitHub URL")
    technologies = models.CharField(max_length=200, help_text="Comma-separated list of technologies used")
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, help_text="Featured projects will be displayed first")
    display_order = models.IntegerField(default=0, help_text="Higher number displays first")

    class Meta:
        ordering = ['-display_order', '-created_at']

    def __str__(self):
        return self.title

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('website', 'Personal Website'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    display_name = models.CharField(max_length=50, blank=True, help_text="Custom display name (optional)")
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0, help_text="Higher number displays first")
    
    class Meta:
        ordering = ['-display_order', 'platform']
    
    def __str__(self):
        if self.display_name:
            return f"{self.get_platform_display()} - {self.display_name}"
        return self.get_platform_display()