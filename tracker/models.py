from django.db import models

# Create your models here.

class TimeEntry(models.Model):
    description = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.description
    
    def duration(self):
        return self.end_time - self.start_time