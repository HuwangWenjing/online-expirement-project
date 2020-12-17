import hashlib
from django.contrib.auth.hashers import make_password
from job.models import teacher, sign
from job.serializers import SignSer
from rest_framework.views import APIView, Response
from django.utils import timezone
import time
from django.db.models import Avg, Sum
from job.views import t_chk_token, chk_course_id


应该增加学生端签到列表的显示。若过期直接不会显示过来


class student_sign(APIView):
    def post(self, request):
        token=request.META.get('token')
        signno=request.GET.get('signno')
        signtime=request.GET.get('signtime')

        #更新原有记录
