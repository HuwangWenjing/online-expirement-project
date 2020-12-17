from job.models import student
from job.serializers import CouSer
from rest_framework.views import APIView, Response
from django.utils import timezone
from job.views import s_chk_token, chk_course_id

# 学生端主页-课程列表
class student_homepage(APIView):
    def get(self, request):
        token = request.META.get('token')
        cou_id = request.GET.get('course_id')
        print(token)
        print(cou_id)

        stu_id = s_chk_token(token)
        if isinstance(stu_id, Response):
            return stu_id
        s = student.objects.get(pk=stu_id)

        c = chk_course_id(cou_id)
        if isinstance(c, Response):
            return c
        sh = student.objects.filter(StuNo=s, CuNo=c)
        if sh:
            sh = sh.get()
            sh.last_modified = timezone.now()
            sh.save()
        else:
            sh = student.objects.create(StuNo=s, CuNo=c)

        return Response({
            'info': 'success',
            'code': 200,
            'data': CouSer(sh).data
        }, status=200)