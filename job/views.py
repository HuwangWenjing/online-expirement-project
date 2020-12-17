import hashlib
from job.models import teacher, manager, student, course, question, token, homework, submission
from rest_framework.views import APIView, Response
from django.utils import timezone
import time
from django.db.models import Avg, Sum

# a = request.POST.get('前端传过来的参数:这应该是教师登录的页面')
# role= 1,2,3
# if a 是老师字段1:
#     查老师表
#         if 用户名密码正确
#             登录并生成token
#         else
#             返回错误信息
#
# elif 是学生字段
#     ......

def md5(user):
    """md5 加密token"""
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()

def t_chk_token(token):
    if token is None:
        return Response({
            'info': '用户未登录',
            'code': 403
        }, status=403)
    t = token.objects.filter(token=token)
    if len(t) <= 0:
        # token无效
        return Response({
            'info': '无效用户',
            'code': 403
        }, status=403)
    return t.get().tuser.ok


# 教师端-作业
class homework(APIView):
    def get(self, request):
        token = request.META.get('token')


class sign(APIView):
    def get(self, request):
        token = request.META.get('token')


def s_chk_token(token):
    if token is None:
        return Response({
            'info': '用户未登录',
            'code': 403
        }, status=403)
    t = token.objects.filter(token=token)
    if len(t) <= 0:
        # token无效
        return Response({
            'info': '无效用户',
            'code': 403
        }, status=403)
    return t.get().suser.ok


def m_chk_token(token):
    if token is None:
        return Response({
            'info': '用户未登录',
            'code': 403
        }, status=403)
    t = token.objects.filter(token=token)
    if len(t) <= 0:
        # token无效
        return Response({
            'info': '无效用户',
            'code': 403
        }, status=403)
    return t.get().muser.ok

def chk_course_id(course_id):
    try:
        c = course.objects.get(pk=course_id)
    except:
        return Response({
            'info': '该课程不存在',
            'code': 403,
        }, status=403)
    return c

def chk_homework_id(homework_id):
    try:
        h = homework.objects.get(pk=homework_id)
    except:
        return Response({
            'info': '该作业不存在',
            'code': 403,
        }, status=403)
    return h

def chk_submission_id(submission_id):
    try:
        s = submission.objects.get(pk=submission_id)
    except:
        return Response({
            'info': '该提交不存在',
            'code': 403,
        }, status=403)
    return s

# def get_now_time():
#     """获取当前时间"""
#     from django.utils import timezone
#     import pytz
#     tz = pytz.timezone('Asia/Shanghai')
#     # 返回时间格式的字符串
#     now_time = timezone.now().astimezone(tz=tz)
#     now_time_str = now_time.strftime("%Y.%m.%d %H:%M:%S")
#
#     # 返回datetime格式的时间
#     now_time = timezone.now().astimezone(tz=tz).strftime("%Y-%m-%d %H:%M:%S")
#     now = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')


from .View.tea_homepage import teacher_homepage
from .View.login import login
from .View.stu_homepage import student_homepage


