from django.contrib import admin
from django.utils.html import format_html
from .models import (
    UserProfile,
    Instructor,
    Student,
    Course,
    Tag,
    Prerequisites,
    Learning,
    Video,
    Schedule,
    Class,
    Enrollment,
    Payment,
    Usercourse,
    Recording,
    Review,
    ClassFeedback)



class TagAdmin(admin.TabularInline):
    model = Tag
    
class PrerequisitesAdmin(admin.TabularInline):
    model = Prerequisites
    
class LearningAdmin(admin.TabularInline):
    model = Learning 
    
class VideoAdmin(admin.TabularInline):
    model = Video
    
class RecordAdmin(admin.TabularInline):
    model = Recording
    
class CoursesAdmin(admin.ModelAdmin): 
    inlines = [TagAdmin,PrerequisitesAdmin,LearningAdmin,VideoAdmin,RecordAdmin]
    list_display = ['title','get_price','get_discount','is_published']
    list_filter = ('discount','is_published')
    
    def get_price(self,course):
        return f'{course.price} ₹'
    
    def get_discount(self,course):
        return f'{course.discount} %'
    
    get_discount.short_description = 'discount'
    get_price.short_description = 'price'
    
class ClassAdmin(admin.ModelAdmin):
    list_display = ['course', 'display_schedules']

    def display_schedules(self, obj):
        schedules = obj.course.schedule_set.all()
        schedule_list = ', '.join([str(schedule) for schedule in schedules])

        return schedule_list

    display_schedules.short_description = 'Schedules'
    
class InstructorAdmin(admin.ModelAdmin):
    list_display =['user_profile','first_name','last_name','rating'] 
    list_filter = ['rating']
       
class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ('order_id','get_user', 'get_course','status')
    list_filter = ('course','status')
    
    def get_user(self,payment):
        return format_html(f"<a target='_blank' href ='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")
    
    def get_course(self,payment):
        return format_html(f"<a target='_blank' href ='/admin/onlineclasses/course/{payment.course.id}'>{payment.course}</a>")
    
    get_course.short_description = 'Course'
    get_user.short_description = 'User'
    
    
class UsercourseAdmin(admin.ModelAdmin):
    model = Usercourse
    list_display = ('click','get_user', 'get_course')
    list_filter = ['course']
    
    def get_user(self,usercourse):
        return format_html(f"<a target='_blank' href ='/admin/auth/user/{usercourse.user.id}'>{usercourse.user}</a>")
    
    def click(self, usercourse):
        return 'Click to Open'
    
    def get_course(self,usercourse):
        return format_html(f"<a target='_blank' href ='/admin/onlineclasses/course/{usercourse.course.id}'>{usercourse.course}</a>")
    
    get_course.short_description = 'Course'
    get_user.short_description = 'User'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','title','is_instructor']
    list_filter = ['is_instructor']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user_profile','name','email']
    
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student','email', 'enrolled_class','instructor_name','enrollment_date','status','notification')
    list_filter = ['enrolled_class']
    
    def instructor_name(self, obj):
        return obj.enrolled_class.schedule.instructor

    instructor_name.short_description = 'Instructor'

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['instructor','course','class_date','enrolled_students','start_time','end_time']
    list_filter = ['course','instructor']
    
    def enrolled_students(self, obj):
        return ', '.join([f"{enrollment.student.first_name} {enrollment.student.last_name}" for enrollment in obj.enrollment_set.all()])

    enrolled_students.short_description = 'Enrolled Students'
    
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title','video','course','serial_number','created_at','updated_at']
 
class RecordingAdmin(admin.ModelAdmin):
    list_display = ['title','course','instructor','serial_number'] 
    list_filter = ['course','instructor']
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['student','course','rating']
    list_filter = ['course','rating']
class ClassFeedbackAdmin(admin.ModelAdmin):
    list_display = ['class_instance','schedule_instance','student','rating']
    list_filter = ['rating','class_instance']
 
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CoursesAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(Class,ClassAdmin)
admin.site.register(Enrollment,EnrollmentAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Usercourse,UsercourseAdmin)
admin.site.register(Recording,RecordingAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(ClassFeedback,ClassFeedbackAdmin)
