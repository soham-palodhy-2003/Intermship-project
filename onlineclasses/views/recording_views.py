from django.shortcuts import render, redirect
from onlineclasses.models import Class, Recording
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def play_recorded_classes(request,recording_id):
    recording = get_object_or_404(Recording, id=recording_id)
    return render(request, 'courses/view_recorded_classes.html', {'recording': recording})
