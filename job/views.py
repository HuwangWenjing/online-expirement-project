import hashlib
from django.contrib.auth.hashers import make_password
from job.models import teacher, manager, student, course, question, token, homework
from job.serializers import MaInfoSer, TeaInfoSer, StuInfoSer, CouSer, HomSer
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

def chk_course_id(cou_id):
    try:
        c = course.objects.get(pk=cou_id)
    except:
        return Response({
            'info': '该课程不存在',
            'code': 403,
        }, status=403)
    return c





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





