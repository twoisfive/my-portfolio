import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=False)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None
    
    
class Project(models.Model):
    ROLE_CHOICES = [
        ('frontend', 'Frontend Developer'),
        ('backend', 'Backend Developer'),
        ('fullstack', 'Full-Stack Developer'),
        ('mobile', 'Mobile Developer'),
        ('designer', 'UI/UX Designer'),
        ('data', 'Data Engineer/Analyst'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='fullstack')
    tech_stack = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated, e.g. 'React, Django, PostgreSQL'"
    )
    thumbnail = models.URLField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    repo_url = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=False)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]
    
