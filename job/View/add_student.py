from django.shortcuts import render

from job.models import *

def add_student(request):

    Major = (
        '信息管理与信息系统', '计算机科学', '电子商务',
        '会计', '金融学', '法学',
        '英语', '汉语文学',
    )
    sex = ('男', '女')

    is_add = True

    StuNo = request.POST.get('StuNo')
    StuName = request.POST.get('StuName')
    StuSex = request.POST.get('StuSex')
    StuPassWord = request.POST.get('StuPassWord')
    Major = request.POST.get('Major')
    student.objects.create(
        StuNo=StuNo, StuName=StuName,StuSex=StuSex,Major=Major,StuPassWord=StuPassWord,
    )
    user.objects.create(
        account=StuNo, password=StuPassWord, identity='学生', name=StuName,
    )


    return render(request, 'teacher/add_student.html', {'sex': sex,'Major': Major,'is_add': is_add})
