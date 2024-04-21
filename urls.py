from django.conf import settings
from django.urls import include, path,re_path
from django.conf.urls.static import static
from onlineclasses.views.all_reviews import course_reviews,class_reviews
from onlineclasses.views.livestream import chat_view, streaming_view
from onlineclasses.views import home,verifypayment,my_courses
from onlineclasses.views.courses import course_page,course_overview
from onlineclasses.views.contact_us import contact_us
from onlineclasses.views.enrollment_views import enroll_in_class
from onlineclasses.views.feedback import course_review
from onlineclasses.views.instructor_interface import instructor_interface,schedule_list
from onlineclasses.views.upload_video import upload_recorded_class,upload_lecture
from onlineclasses.views.recording_views import play_recorded_classes
from onlineclasses.views.explore_courses import explore_courses
from onlineclasses.views import SignupView,LoginView,signout,checkout
from onlineclasses.views import submit_rating_feedback,class_feedback
from onlineclasses.views import top_rated
from onlineclasses.views.auth import(
                CustomPasswordResetView,
                CustomPasswordResetDoneView,
                CustomPasswordResetConfirmView,
                CustomPasswordResetCompleteView
)


from onlineclasses.consumers import StreamingConsumer,ChatConsumer
websocket_urlpatterns = [
    re_path(r'^streaming/$', StreamingConsumer.as_asgi()),
     re_path(r'ws/chat/(?P<room_name>\w+)/$',ChatConsumer.as_asgi()),
]

urlpatterns = [
    path("", home, name='home'),
    path('streaming/', streaming_view, name='streaming'),
    path('chat/<str:room_name>/', chat_view, name='chat_view'),
    path("logout", signout, name='logout'),
    path("my_courses", my_courses, name='my_courses'),
    path("signup", SignupView.as_view(), name='Signup'),
    path("login", LoginView.as_view(), name='login'),
    path("contact_us/", contact_us, name='contact_us'),
    path('schedule/create/', instructor_interface, name='create_schedule'),
    path('schedule/list/', schedule_list, name='schedule_list'),
    path('enroll-class/', enroll_in_class, name='enroll_class'),
    path('upload-class/',upload_recorded_class, name='upload_recorded_class'),
    path('upload-lecture/',upload_lecture, name='upload_lecture'),
    path('play-recorded-class/<int:recording_id>/', play_recorded_classes, name='play_recorded_class'),
    path("explore_courses", explore_courses, name='explore_courses'),
    path("courses/<str:slug>/overview/", course_overview, name='course_overview'),
    path("courses/<str:slug>/", course_page, name='course_page'),
    path("checkout/<str:slug>", checkout, name='checkout_page'),
    path('course/<int:course_id>/review/', course_review, name='course_review'),
    path('submit-rating-feedback/', submit_rating_feedback, name='submit_rating_feedback'),
     path('class-feedback/', class_feedback, name='class_feedback'),
     path('top_rated/', top_rated, name='top_rated'),
     path('course-reviews/', course_reviews, name='course-reviews'),
     path('class-reviews/', class_reviews, name='class-reviews'),
    path("verify_payment", verifypayment, name='verify_payment'),
    
    path("reset_password/",CustomPasswordResetView.as_view(template_name = "courses/password_reset.html"),
         name='password_reset'),
    path("reset_password_sent/",CustomPasswordResetDoneView.as_view(template_name = "courses/password_reset_sent.html"), 
         name='password_reset_done'),
    path("reset/<uidb64>/<token>/",CustomPasswordResetConfirmView.as_view(template_name = "courses/password_reset_form.html"),
         name='password_reset_confirm'),
    path("reset_password_complete/",CustomPasswordResetCompleteView.as_view(template_name = "courses/password_reset_complete.html"),
         name='password_reset_complete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)