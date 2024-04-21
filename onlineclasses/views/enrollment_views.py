from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from onlineclasses.models import Class, Enrollment, Schedule, Student, UserProfile, Course, Instructor
from onlineclasses.forms import EnrollmentForm
from django.contrib import messages


@login_required
def enroll_in_class(request):
    available_classes = Class.objects.filter(
        student=request.user, enrollment__status='approved')
    available_schedules = Schedule.objects.filter(
        course__in=available_classes.values('course'))
    instructors = Instructor.objects.all()
    paid_courses = Course.objects.filter(
        usercourse__user=request.user, usercourse__date__isnull=False)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)

        if form.is_valid():
            enrolled_class_id = form.cleaned_data['enrolled_class'].id
            enrolled_class = Class.objects.get(id=enrolled_class_id)
            selected_instructor = form.cleaned_data['instructor']
            selected_schedules = form.cleaned_data['schedule']
            
            for schedule in selected_schedules:
                if enrolled_class.enrollment_set.filter(student=request.user, enrolled_class__course=enrolled_class.course, enrolled_class__schedule=schedule).exists():
                    error_message = 'You are already enrolled in one of the selected schedules.'
                    return render(request, 'courses/enroll_class.html', {'form': form, 'classes': available_classes, 'schedules': available_schedules, 'instructors': instructors, 'error_message': error_message})
            
            if enrolled_class.course in paid_courses:
                student_name = form.cleaned_data['student_name']
                email = form.cleaned_data['email']

                for schedule in selected_schedules:
                    enrollment = Enrollment.objects.create(
                        student=request.user,
                        email=email,
                        enrolled_class=enrolled_class,
                        status='approved'
                    )
                    enrollment.notification = True
                    enrollment.save()
                    
                    enrollment.schedule.set(selected_schedules)

                return render(request, template_name='courses/enrollment_success.html', context={'enrollment': enrollment})

    else:
        form = EnrollmentForm()

    return render(request, 'courses/enroll_class.html', {'form': form, 'classes': available_classes, 'schedules': available_schedules, 'instructors': instructors})
