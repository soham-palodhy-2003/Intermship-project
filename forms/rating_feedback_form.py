from django import forms
from onlineclasses.models import Review,Student


class RatingFeedbackForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    class Meta:
        model = Review
        fields = ['name','email','course','rating','comment']
        labels = {
            'course': 'Course',
            'rating': 'Rating',
            'comment': 'Comment',
        }