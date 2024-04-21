from django import forms
from onlineclasses.models import Video

class UploadLectureForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        label='Description'
    )   
    class Meta:
        model = Video
        
        fields = ['title','description','video','course','serial_number']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'video': 'Video',
            'course': 'Course',
            'serial_number': 'Serial Number'
        }
