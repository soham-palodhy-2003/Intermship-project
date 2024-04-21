from django.shortcuts import render
from onlineclasses.models import Review, ClassFeedback

def course_reviews(request):
    course_reviews = Review.objects.all()

    return render(request, 'courses/course_reviews.html', {
        'course_reviews': course_reviews,
    })
    
def class_reviews(request):
    class_feedback_reviews = ClassFeedback.objects.all()

    return render(request, 'courses/class_reviews.html', {
        'class_feedback_reviews': class_feedback_reviews,
    })
