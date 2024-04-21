from django import forms
from onlineclasses.models import Recording

class RecordedClassForm(forms.ModelForm):
    class Meta:
        model = Recording
        fields = ['title', 'description', 'course', 'instructor', 'video_file','serial_number']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'course': 'Course',
            'instructor': 'Instructor',
            'video_file': 'Video File',
            'serial_number': 'Serial Number'
        }
