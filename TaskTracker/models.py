from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    #defines the various title choices.
    TITLE_CHOICES = [
        ('urgent_important', 'Urgent & Important'),
        ('not_urgent_important', 'Not Urgent but Important'),
        ('urgent_not_important', 'Urgent but Not Important'),
        ('not_urgent_not_important', 'Not Urgent & Not Important'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50, choices=TITLE_CHOICES)
    status = models.CharField(
        max_length=20,
        choices=[
            ('todo', 'To Do'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
        ],
        default='todo',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
