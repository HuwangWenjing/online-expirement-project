from job.models import teacher, course
from job.serializers import CouSer
from rest_framework.views import APIView, Response
from job.views import t_chk_token

# 教师端主页-课程列表
class teacher_course(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')

        tea_id = t_chk_token(token)
        if isinstance(tea_id, Response):
            return tea_id

        course_list = teacher.objects.get(pk=tea_id).teacher_courses.all()

        return Response({
            'info': 'success',
            'code': 200,
            'data': CouSer(course_list, many=True).data
        }, status=200)