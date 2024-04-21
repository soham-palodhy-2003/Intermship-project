from django.shortcuts import render
from onlineclasses.models import Instructor, Course, ClassFeedback,Schedule

def top_rated(request):
    top_courses = Course.objects.filter(rating__gte=4.0).order_by('-rating')
    top_class_feedbacks = ClassFeedback.objects.filter(rating__gte=4.0).order_by('-rating').select_related('class_instance__course', 'schedule_instance__instructor')


    context = {
        'top_courses': top_courses,
        'top_class_feedbacks': top_class_feedbacks,
    }

    return render(request, 'courses/top_rated.html', context)
