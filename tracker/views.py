from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TimeEntry
from .forms import TimeEntryForm

def time_tracker(request):
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('time_tracker')
    else:
        form = TimeEntryForm()
    entries = TimeEntry.objects.all()
    return render(request, 'calculator/time_tracker.html', {'form': form, 'entries': entries})