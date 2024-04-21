from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from onlineclasses.forms import RatingFeedbackForm, ClassFeedbackForm
from onlineclasses.models import Course, Review, Student, UserProfile, Class, Schedule, ClassFeedback


def course_review(request, course_id):
    if not request.user.is_authenticated:
        return redirect('login')
    course = Course.objects.get(pk=course_id)

    form = RatingFeedbackForm(initial={'course': course})

    context = {
        'course': course,
        'form': form,
    }

    return render(request, 'courses/course_review.html', context)


def class_feedback(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = ClassFeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.name = form.cleaned_data['name']
            feedback.email = form.cleaned_data['email']

            try:
                user_profile = UserProfile.objects.get(user=request.user)
                student = Student.objects.get(user_profile=user_profile)
                feedback.student = student
                selected_class = form.cleaned_data['class_id']
                selected_schedule = form.cleaned_data['schedule_id']

                class_feedback, _ = ClassFeedback.objects.get_or_create(
                    class_instance=selected_class,
                    schedule_instance=selected_schedule,
                    student=student,
                )

                class_feedback.feedback_text = form.cleaned_data['feedback_text']
                class_feedback.rating = form.cleaned_data['rating']
                class_feedback.save()

                return HttpResponse('Feedback approved!')
            except UserProfile.DoesNotExist:
                messages.error(request, 'User profile does not exist.')
            except Student.DoesNotExist:
                messages.error(request, 'Student does not exist.')

    else:
        form = ClassFeedbackForm()

    return render(request, "courses/class_feedback.html", {'form': form})


def submit_rating_feedback(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = RatingFeedbackForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.name = form.cleaned_data['name']
            review.email = form.cleaned_data['email']
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                student = Student.objects.get(user_profile=user_profile)
                review.student = student
                review.save()
                return HttpResponse('Feedback approved!')
            except UserProfile.DoesNotExist:
                print("user profile not found")

                messages.error(request, 'User profile does not exist.')
            except Student.DoesNotExist:
                print('student does not exist')

                messages.error(request, 'Student does not exist.')

    return render(request, "courses/course_page.html")
