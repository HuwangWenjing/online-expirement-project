from job.models import question, homework
from job.serializers import HomSer
from rest_framework.views import APIView, Response

# 学生提交作业
class handin_homework(APIView):
    def post(self, request):
        token = request.META.get('token')
        homno = request.POST.get('homno')
        quesno = request.POST.get('quesno')
        stuans = request.POST.get('stuans')
        subtime = request.POST.get('subtime')
        ansnums = request.POST.get('ansnums').strip() #获取题目数量

        sh = homework.objects.create(
            Homno = homno,
            SubTime = subtime,
        )

        # 向question中批量添加记录
        if ansnums.isdigit() and int(ansnums) > 0:
            submission_list = []
            for i in range(int(ansnums)):
                submission_list.append(
                    question(
                        QuesNo=quesno,
                        Ans=stuans,
                        HomNo=sh,
                    )
                )
            s= question.objects.bulk_create(submission_list)  # 使用django.db.models.query.QuerySet.bulk_create()批量创建对象，减少SQL查询次数
            return Response({
                'info': 'success',
                'code': 200,
                'data': HomSer(sh, s)
            }, status=200)

        else:
            return Response({
                'info': '未填写答案',
                'code': 400
            }, status=400)