import hashlib
from django.contrib.auth.hashers import make_password
from job.models import teacher, token, homework, manager, student, course, question
from job.serializers import MaInfoSer, TeaInfoSer, StuInfoSer, HomSer,CouSer
from rest_framework.views import APIView, Response
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
import time

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


class login(APIView):
    def get(self, request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        ro = request.POST.get('role')
        print(uname)
        print(pwd)
        print(ro)

        if not all([uname, pwd]):
            return Response({
                'info': '参数不完整',
                'code': 400
            }, status=400)

        if ro ==1:
            try:
                muser= manager.objects.get(MaNo = uname)
            except:
                return Response({
                    'info': '用户名不存在',
                    'code': 403
                }, status=403)
            if muser.check_pwd(pwd):
                # 登录成功后生成token
                token = md5(muser)
                token.objects.update_or_create(muser=muser, defaults={'token': token})
                res = {'info': 'success', 'token': token, 'code': 200, 'data': MaInfoSer(muser).data}
                return Response(res)
            else:
                return Response({
                    'info': '密码错误',
                    'code': 403
                }, status=403)

        elif ro ==2:
            try:
                tuser= teacher.objects.get(TeaNo = uname)
            except:
                return Response({
                    'info': '用户名不存在',
                    'code': 403
                }, status=403)
            if tuser.check_pwd(pwd):
                # 登录成功后生成token
                token = md5(tuser)
                token.objects.update_or_create(tuser=tuser, defaults={'token': token})
                res = {'info': 'success', 'token': token, 'code': 200, 'data': TeaInfoSer(tuser).data}
                return Response(res)
            else:
                return Response({
                    'info': '密码错误',
                    'code': 403
                }, status=403)

        else:
            try:
                suser = student.objects.get(StuNo=uname)
            except:
                return Response({
                    'info': '用户名不存在',
                    'code': 403
                }, status=403)
            if suser.check_pwd(pwd):
                # 登录成功后生成token
                token = md5(suser)
                token.objects.update_or_create(suser=suser, defaults={'token': token})
                res = {'info': 'success', 'token': token, 'code': 200, 'data': StuInfoSer(suser).data}
                return Response(res)
            else:
                return Response({
                    'info': '密码错误',
                    'code': 403
                }, status=403)


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

class teacher_homepage(APIView):
    def get(self, request):
        token = request.META.get('token')
        cou_id = request.GET.get('course_id')
        print(token)
        print(cou_id)

        tea_id = t_chk_token(token)
        if isinstance(tea_id, Response):
            return tea_id
        t = teacher.objects.get(pk=tea_id)

        c = chk_course_id(cou_id)
        if isinstance(c, Response):
            return c
        th = teacher.objects.filter(TeaNo=t, CuNo=c)
        if th:
            th = th.get()
            th.last_modified = timezone.now()
            th.save()
        else:
            th = teacher.objects.create(TeaNo=t, CuNo=c)

        return Response({
            'info': 'success',
            'code': 200,
            'data': CouSer(th).data
        }, status=200)


class publish_homework(APIView):
    def get(self, request):
        token = request.META.get('token')
        homno = request.POST.get('homno')
        title = request.POST.get('title')
        pubdate = request.POST.get('pubdate')
        quesno = request.POST.get('quesno')
        cont = request.POST.get('cont')
        corans = request.POST.get('corans')
        nums = request.POST.get('nums').strip() #获取题目数量
        print(token)
        print(homno)
        print(title)
        print(pubdate)
        print(cont)
        print(corans)
        print(nums)

        # 1. 查token表 判断是哪个用户在操作
        # 2. 根据查表结果 判断是否合法
        tea_id = t_chk_token(token)
        if isinstance(tea_id, Response):
            return tea_id

        # 如何同时向homework和question中添加记录
        h = homework.objects.create(
            Title = title,
            PubDate = pubdate,

        )

        # 向question中批量添加记录
        if nums.isdigit() and int(nums) > 0:

            question_list = []
            for i in range(int(nums)):
                question_list.append(
                    question(
                        QuesNo=quesno,
                        Cont=cont,
                        Corans=corans
                    )
                )
            question.objects.bulk_create(question_list)  # 使用django.db.models.query.QuerySet.bulk_create()批量创建对象，减少SQL查询次数
            #messages.info(request, '批量添加{}条数据完成！'.format(nums))


        return Response({
            'info': 'success',
            'code': 200,
            'data': HomSer(h).data
        }, status=200)




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





