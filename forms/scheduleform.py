from django import forms
from onlineclasses.models import Schedule, Instructor, Course


class ScheduleForm(forms.ModelForm):
    AMPM_CHOICES = [
        ('AM', 'AM'),
        ('PM', 'PM'),
    ]

    start_time = forms.TimeField(widget=forms.TimeInput(
        format='%I:%M %p'), help_text='Enter the starting time')
    start_time_ampm = forms.ChoiceField(choices=AMPM_CHOICES)
    end_time = forms.TimeField(widget=forms.TimeInput(
        format='%I:%M %p'), help_text='Enter the ending time')
    end_time_ampm = forms.ChoiceField(choices=AMPM_CHOICES)
    course = forms.ModelChoiceField(queryset=Course.objects.all())

    class Meta:
        model = Schedule
        fields = ['class_date', 'start_time', 'end_time', 'availability']
        widgets = {
            'class_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'})
        }

        help_texts = {
            'class_date': 'Enter the date in the format DD-MM-YYYY',
        }
