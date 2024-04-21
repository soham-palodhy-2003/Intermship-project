from onlineclasses.views.homepage import home
from onlineclasses.views.courses import course_page,my_courses,course_overview
from onlineclasses.views.instructor_interface import instructor_interface,schedule_list
from onlineclasses.views.enrollment_views import enroll_in_class
from onlineclasses.views.recording_views import play_recorded_classes
from onlineclasses.views.checkout import checkout,verifypayment
from onlineclasses.views.explore_courses import explore_courses
from onlineclasses.views.auth import SignupView
from onlineclasses.views.auth import LoginView,signout
from onlineclasses.views.feedback import course_review,submit_rating_feedback,class_feedback
from onlineclasses.views.highlight import top_rated
from onlineclasses.views.all_reviews import course_reviews,class_reviews
from onlineclasses.views.upload_video import upload_recorded_class,upload_lecture

from onlineclasses.views.livestream import streaming_view,chat_view
#from onlineclasses.views.livestream import record_live_stream,start_recording,stop_recording,streaming_message,chat_message
from onlineclasses.views.auth import CustomPasswordResetView,CustomPasswordResetDoneView,CustomPasswordResetConfirmView,CustomPasswordResetCompleteView

__all__ = [
    'home',
    'SignupView',
    'LoginView',
    'signout',
    'explore_courses',
    'instructor_interface',
    'create_schedule',
    'schedule_list',
    'enroll_in_class',
    'checkout',
    'verifypayment',
    'CustomPasswordResetView',
    'CustomPasswordResetDoneView',
    'CustomPasswordResetConfirmView',
    'CustomPasswordResetCompleteView',

]