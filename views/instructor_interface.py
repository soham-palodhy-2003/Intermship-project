from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from onlineclasses.forms.scheduleform import ScheduleForm
from onlineclasses.models import UserProfile, Schedule, Instructor, Course, Enrollment


@login_required
def instructor_interface(request):
    try:
        user_profile = request.user.userprofile
        instructor, created = Instructor.objects.get_or_create(
            user_profile=user_profile)
        courses = Course.objects.all()

        if request.method == 'POST':
            form = ScheduleForm(request.POST)
            if form.is_valid():
                schedule = form.save(commit=False)
                schedule.instructor = instructor
                schedule.course = form.cleaned_data['course']
                schedule.save()
                return redirect('schedule_list')
        else:
            form = ScheduleForm()

        schedules = Schedule.objects.filter(instructor=instructor)
        return render(request, 'courses/instructor_interface.html', {'form': form, 'schedules': schedules, 'courses': courses})

    except Instructor.DoesNotExist:
        return redirect('login')


def schedule_list(request):
    schedules = Schedule.objects.all()
    courses = Course.objects.all()

    is_instructor = False
    user_profile = None
    user_classes = set()
    enrolled_class_ids = []  

    try:
        user_profile = request.user.userprofile
        is_instructor = user_profile.is_instructor

        if is_instructor:
            user_classes = set(schedules.filter(
                instructor__user_profile=user_profile))
        elif user_profile.student:
            enrolled_classes = Enrollment.objects.filter(student=request.user)
            enrolled_class_ids = [
                enrolled_class.enrolled_class.schedule.id for enrolled_class in enrolled_classes]
            print("DEBUG: is_enrolled =", enrolled_class_ids)
    except UserProfile.DoesNotExist:
        pass

    return render(request, 'courses/schedule_list.html', {
        'schedules': schedules,
        'courses': courses,
        'is_instructor': is_instructor,
        'enrolled_class_ids': enrolled_class_ids,
        'user_classes': user_classes
    })
