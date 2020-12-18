from job.models import teacher
from job.serializers import TeacherSer
from rest_framework.views import APIView, Response
from django.utils import timezone
from job.views import t_chk_token, chk_course_id


# 教师端主页-课程列表
class teacher_homepage(APIView):
    def get(self, request):
        token = request.META.get('token')
        cou_id = request.GET.get('course_id')

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
            'data': TeacherSer(th).data
        }, status=200)