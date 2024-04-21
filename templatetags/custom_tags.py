from django import template
import math
from onlineclasses.models import Usercourse,Course,Enrollment
register = template.Library()
@register.simple_tag

def cal_sale_price(price,discount):
    if discount is None or discount == 0:
        return price
    sellPrice = price-(price * (discount * 0.01))
    return math.floor(sellPrice)

@register.filter
def rupee(price):
    rupee_price = price 
    return f'₹{rupee_price}'

@register.simple_tag

def is_enrolled(request,course):
    user = None
    if not request.user.is_authenticated:
        return False
    user = request.user
    try:
        user_course = Usercourse.objects.get(user=user,course=course)
        return True
    except:
        return False
    
@register.filter
def schedule(user, schedule_id):
    if user.userprofile.is_instructor:
        return False

    try:
        enrollment = Enrollment.objects.filter(student=user, enrolled_class__schedule_id=schedule_id)
        return enrollment.exists()
    except Enrollment.DoesNotExist:
        return False