from job.models import student
from job.serializers import StudentSer, CouSer
from rest_framework.views import APIView, Response
from django.utils import timezone
from job.views import s_chk_token, chk_course_id

# 学生端主页-课程列表
class student_course(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')

        stu_id = s_chk_token(token)
        if isinstance(stu_id, Response):
            return stu_id

        course_list = student.objects.get(pk=stu_id).CourseNo.all()

        return Response({
            'info': 'success',
            'code': 200,
            'data': CouSer(course_list, many=True).data
        }, status=200)