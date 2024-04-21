from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from onlineclasses.forms import RecordedClassForm,UploadLectureForm
from onlineclasses.models import Recording
from django.http import HttpResponse
from django.contrib import messages

@login_required
def upload_recorded_class(request):
    if request.method == 'POST':
        form = RecordedClassForm(request.POST, request.FILES)
        if form.is_valid():
            recorded_class = form.save(commit=False)
            recorded_class.instructor = request.user.userprofile.instructor
            recorded_class.save()
            messages.success(request, 'Recorded class uploaded successfully!')
            return redirect('upload_recorded_class')
    else:
        form = RecordedClassForm()
    
    return render(request, 'courses/upload_recorded_class.html', {'form': form})

@login_required
def upload_lecture(request):
    if request.method == 'POST':
        form = UploadLectureForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            messages.success(request, 'Lecture uploaded successfully!')
            return redirect('upload_lecture')  
    else:
        form = UploadLectureForm()
    return render(request, 'courses/upload_lecture_videos.html', {'form': form})