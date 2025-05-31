from django.db import models

# Create your models here.
class Task(models.Model):
    status_choices = [
        ('pending', "Pending"),
        ('in_progress','In Progress'),
        ('completed','Completed')
    ]
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    creation_date = models.DateTimeField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length = 20, choices=status_choices )

    def __str__(self):
        return self.name