from django import forms
from onlineclasses.models import Class, Student, Course, Schedule, Instructor

class EnrollmentForm(forms.Form):
    student_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    enrolled_class = forms.ModelChoiceField(queryset=Class.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all())
    schedule = forms.ModelMultipleChoiceField(queryset=Schedule.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    def clean_student_name(self):
        student_name = self.cleaned_data['student_name']
        # Add any custom validation for student name if needed
        return student_name

    def clean_email(self):
        email = self.cleaned_data['email']
        # Add any custom validation for email if needed
        return email

    def clean(self):
        cleaned_data = super().clean()
        # Perform any additional validation for the overall form if needed
        return cleaned_data
