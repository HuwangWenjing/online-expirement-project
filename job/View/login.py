from job.models import teacher, manager, student
from rest_framework.views import APIView, Response
from job.views import md5


# 三类用户登录视图
class login(APIView):
    authentication_classes = []

    def get(self, request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        ro = request.POST.get('role')

        if not all([uname, pwd]):
            return Response({
                'info': '参数不完整',
                'code': 400
            }, status=400)

        if ro == 1:
            try:
                m= manager.objects.get(MaNo = uname)
            except:
                return Response({
                    'info': '用户名不存在',
                    'code': 403
                }, status=403)
            if pwd == m.MPassword:
                # 登录成功后生成token
                token = md5(m)
                token.objects.update_or_create(muser=uname, defaults={'token': token})
                res = {'info': 'success', 'token': token, 'code': 200, 'data': MaInfoSer(m).data}
                return Response(res)
            else:
                return Response({
                    'info': '密码错误',
                    'code': 403
                }, status=403)

        elif ro == 2:
            try:
                t= teacher.objects.get(TeaNo = uname)
            except:
                return Response({
                    'info': '用户名不存在',
                    'code': 403
                }, status=403)
            if pwd == t.TPassword:
                # 登录成功后生成token
                token = md5(t)
                token.objects.update_or_create(tuser=uname, defaults={'token': token})
                res = {'info': 'success', 'token': token, 'code': 200, 'data': TeaInfoSer(t).data}
                return Response(res)
            else:
                return Response({
                    'info': '密码错误',
                    'code': 403
                }, status=403)

        else:
            try:
                s = student.objects.get(StuNo=uname)
            except:
                return Response({
                    'info': '用户名不存在',
                    'code': 403
                }, status=403)
            if pwd == s.SPassword:
                # 登录成功后生成token
                token = md5(s)
                token.objects.update_or_create(suser=uname, defaults={'token': token})
                res = {'info': 'success', 'token': token, 'code': 200, 'data': StuInfoSer(s).data}
                return Response(res)
            else:
                return Response({
                    'info': '密码错误',
                    'code': 403
                }, status=403)