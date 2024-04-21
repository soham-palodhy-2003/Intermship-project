from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default='Default Title')
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Instructor(models.Model):
    user_profile = models.OneToOneField(UserProfile,default=None, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=3, decimal_places=1,null = True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Student(models.Model):
    user_profile = models.OneToOneField(UserProfile, default=None,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=100,null=False)
    slug = models.CharField(max_length=100,null=False,unique=True)
    description = models.TextField(max_length=500,null=True)
    thumbnail = models.ImageField(upload_to='files/thumbnail')
    duration = models.PositiveIntegerField(help_text="Duration:")
    price = models.IntegerField(null=False)
    discount = models.PositiveIntegerField(null=False, default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    length = models.PositiveIntegerField(null=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1,null = True)
    
    def __str__(self):
        return self.title
    
class CourseProperty(models.Model):
    title = models.CharField(max_length=50,null=False)
    course = models.ForeignKey(Course, null=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        abstract = True
class Tag(CourseProperty):
    pass
class Prerequisites(CourseProperty):
    pass
class Learning(CourseProperty):
    pass
    
class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='files/videos')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    serial_number = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Schedule(models.Model):
    instructor = models.ForeignKey(Instructor,default=1, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False,default=1)
    class_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    availability = models.PositiveIntegerField(default = 0)
    
    def __str__(self):
        return f'{self.course.title}:- {self.class_date} from {self.start_time} to {self.end_time}'

class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule,null=False, on_delete=models.CASCADE,default = 1)
    student = models.ManyToManyField(User, through='Enrollment')
    rating = models.DecimalField(max_digits=3, decimal_places=1,null = True)
    
    def __str__(self):
        return str(self.course)

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=35,null=False)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    schedule = models.ManyToManyField(Schedule)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notification = models.BooleanField(default=False)
    
    
    def __str__(self):
        schedules = self.schedule.all()
        schedule_details = []
        for schedule in schedules:
            schedule_info = f'Class Date: {schedule.class_date} from {schedule.start_time} to {schedule.end_time}'
            schedule_details.append(schedule_info)
        enrolled_class = self.enrolled_class
        instructor = enrolled_class.schedule.instructor
        return (f'Student: {self.student.first_name} {self.student.last_name} - {enrolled_class.course.title} (course) '
                f'Instructor: {instructor} '
                f'{", ".join(schedule_details)}')

    
class Usercourse(models.Model):
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} {self.course.title}'
    
class Payment(models.Model):
    order_id = models.CharField(max_length=50,null=True)
    payment_id = models.CharField(max_length=50,null=True)
    user_course = models.ForeignKey(Usercourse,null=True,blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
class Recording(models.Model):
    title = models.CharField(max_length=255,default='default')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False,default=1)
    description = models.TextField(blank=True)
    serial_number = models.IntegerField(default=1)
    instructor = models.ForeignKey(Instructor,default = 1,on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='files/live_recordings',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    RATINGS_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATINGS_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.student.name} for {self.course.title}'
    
class ClassFeedback(models.Model):
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE)
    schedule_instance = models.ForeignKey(Schedule, on_delete=models.CASCADE,null = True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1,null = True)

    def __str__(self):
        return f"Feedback for {self.schedule_instance.course.title} - {self.schedule_instance.class_date} by {self.student}"
