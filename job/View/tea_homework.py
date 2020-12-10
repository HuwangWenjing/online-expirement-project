import hashlib
from django.contrib.auth.hashers import make_password
from job.models import teacher, manager, student, course, question, token, homework
from job.serializers import MaInfoSer, TeaInfoSer, StuInfoSer, CouSer, HomSer
from rest_framework.views import APIView, Response
from django.utils import timezone
import time
from django.db.models import Avg, Sum
from job.views import t_chk_token

# 教师发布作业. ##########选择题、判断、填空、问答和编程
class publish_homework(APIView):
    def post(self, request):
        token = request.META.get('token')
        homno = request.POST.get('homno')
        quesno = request.POST.get('quesno')
        type = request.POST.get('type')
        title = request.POST.get('title')
        pubtime = request.POST.get('pubtime')

        cont = request.POST.get('cont')
        corans = request.POST.get('corans')
        score = request.POST.get('score')
        quesnums = request.POST.get('quesnums').strip() #获取题目数量

        # 1. 查token表 判断是哪个用户在操作
        # 2. 根据查表结果 判断是否合法
        tea_id = t_chk_token(token)
        if isinstance(tea_id, Response):
            return tea_id

        ph = homework.objects.create(
            HomNo=homno,
            Title=title,
            PubTime=pubtime,
        )

        # 向question中批量添加记录
        if quesnums.isdigit() and int(quesnums) > 0:
            question_list = []
            for i in range(int(quesnums)):
                question_list.append(
                    question(
                        QuesNo=quesno,
                        Cont=cont,
                        Ans=corans,
                        HomNo=ph,
                        Score=score,
                        isCorrect=True,
                    )
                )
            p = question.objects.bulk_create(question_list)  # 使用django.db.models.query.QuerySet.bulk_create()批量创建对象，减少SQL查询次数
            #messages.info(request, '批量添加{}条数据完成！'.format(nums))
            return Response({
                'info': 'success',
                'code': 200,
                'data': HomSer(ph, p).data
            }, status=200)

        else:
            return Response({
                'info': '不完整',
                'code': 400
            }, status=400)


# 教师手动批改作业   跨表查询
class manual_score(APIView):
    def post(self, request):
        token = request.META.get('token')
        auto = request.POST.get('isAuto')
        nums = request.POST.get('nums')
        quesno = request.POST.get('quesno')
        grade = request.POST.get('grade')
        stuno = request.POST.get('stuno')

        if auto == 0:

            tea_id = t_chk_token(token)
            if isinstance(tea_id, Response):
                return tea_id

            if nums.isdigit() and int(nums) > 0:
                for i in range(int(nums)):
                    q = question.objects.filter(QuesNo=quesno, isCorrect=False)
                    q.Grade = grade
                    q.save()

            stuhom = homework.objects.get(course__StuNo=stuno)  # 取出作业表中某学生的记录
            allquestion = question.objects.filter(homework__course__StuNo=stuno)  # 取出题目表中该学生的所有题
            totalgrade = allquestion.aggregate(Sum('Grade'))  # 对取出来的所有题的成绩字段的值加总
            stuhom.TotalGrade = totalgrade  # 更新TotalGrade字段
            stuhom.save()

            return Response({
                'info': 'success',
                'code': 200,
                'data': HomSer(stuhom)
            }, status=200)


# 系统自动批改作业
class auto_score(APIView):
    def post(self, request):
        auto = request.POST.get('isAuto')
        nums = request.POST.get('nums')
        stuno = request.POST.get('stuno')

        if auto==1: #教师选择自动批改
            #按题目顺序循环
            for i in range(int(nums)):
                #取出学生答案记录isCorrect=False的学生答案和标准答案记录isCorrect=True的标准答案————题号相同
                t=question.objects.get(QuesNo=i, isCorrect=True).Ans
                s=question.objects.get(QuesNo=i, isCorrect=False).Ans
                a=question.objects.get(QuesNo=i, isCorrect=False)
                #取出某道题标准答案的分值
                score= question.objects.get(QuesNo=i).Score
                #比较学生答案和标准答案
                #如果相同：
                if t==s:
                    #满分
                    a.Grade=score
                    a.save()
                #如果不相同：
                else:
                    #零分
                    a.Grade='0'
                    a.save()
            #循环结束，将所有题的分加总得到总分
            stuhom=homework.objects.get(course__StuNo=stuno) #取出作业表中某学生的记录
            allquestion=question.objects.filter(homework__course__StuNo=stuno) #取出题目表中该学生的所有题
            totalgrade=allquestion.aggregate(Sum('Grade')) #对取出来的所有题的成绩字段的值加总
            stuhom.TotalGrade=totalgrade #更新TotalGrade字段
            stuhom.save()

            return Response({
                'info': 'success',
                'code': 200,
                'data': HomSer(stuhom)
            }, status=200)