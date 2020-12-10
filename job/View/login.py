from job.models import teacher, manager, student
from job.serializers import MaInfoSer, TeaInfoSer, StuInfoSer
from rest_framework.views import APIView, Response
from job.views import md5

# 三类用户登录视图
class login(APIView):
    def get(self, request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        ro = request.POST.get('role')

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