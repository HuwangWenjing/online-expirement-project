from job.models import *
from job.serializers import  SignSer, StudentSignSer

from rest_framework.views import APIView, Response

from django.utils import timezone

from job.views import s_chk_token, chk_course_id
class Sign(APIView):#（学生签到）
    def post(self, request):
        token = request.META.get('HTTP_TOKEN')
        course_id = request.GET.get('course_id')

        if course_id is None:
            return Response({
                'info': '参数不完整',
                'code': 400,
            }, status=400)

        student_id = s_chk_token(token)
        if isinstance(student_id, Response):
            return student_id


        Co = chk_course_id(course_id)
        if isinstance(Co, Response):
            return Co

        if studentsign.objects.filter(StuNo=student_id, CuNo=course_id):
            return Response({
                'info': '你已经签过到了',
                'code': 403,
            }, status=403)

        time_now = timezone.now()
        expired_sign = sign.objects.filter( course=course_id, Deadline_lte=time_now)
        #unexpired_sign = sign.objects.filter(student=student_id, course=course_id, Deadline_gt=time_now)
        #expired_sign.isExpiered = True

        if len(expired_sign) > 0:
            return Response({
                'info': '签到已过期',
                'code': 403,
            }, status=403)

        #unexpired_sign.save()
        Ss=studentsign.objects.create(
            StuNo=student_id,
            SubTime = time_now,
            CuNo = course_id,
        )
        return Response({
            'info': 'success',
            'code': 200,
            'data': StudentSignSer(Ss).data
        }, status=200)##

class student_get_sign(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        course_id = request.GET.get('course_id')

        stu_id = s_chk_token(token)
        if isinstance(stu_id, Response):
            return stu_id

        c = chk_course_id(course_id)
        if isinstance(c, Response):
            return c
        time_now = timezone.now()
        expired_sign = sign.objects.filter(course=course_id, Deadline_lte=time_now)
        if len(expired_sign) > 0:
            return Response({
                'info': '签到已过期',
                'code': 403,
            }, status=403)

        Sign = sign.objects.filter(course_id=course_id)

        return Response({
            'info': 'success',
            'code': 200,
            'data': SignSer(Sign).data
        }, status=200)
