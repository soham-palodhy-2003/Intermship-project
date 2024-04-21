from django import forms
from onlineclasses.models import ClassFeedback, Class, Schedule

class ClassFeedbackForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    
    class_id = forms.ModelChoiceField(queryset=Class.objects.all())
    schedule_id = forms.ModelChoiceField(queryset=Schedule.objects.all())

    class Meta:
        model = ClassFeedback
        fields = ['name', 'email', 'class_id', 'schedule_id', 'feedback_text', 'rating']

    def __init__(self, *args, **kwargs):
        super(ClassFeedbackForm, self).__init__(*args, **kwargs)
        self.fields['class_id'].queryset = Class.objects.all()
        self.fields['schedule_id'].queryset = Schedule.objects.all()
