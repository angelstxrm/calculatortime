from django import forms
from .models import TimeEntry

class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ['description', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
