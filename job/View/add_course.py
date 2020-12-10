from django.shortcuts import render

from job.models import *
def add_course(request):
    '''管理员添加课程'''
    is_add = True
    CuNo= request.POST.get('CuNo')
    CuName = request.POST.get('CuName')
   # Major = request.POST.get('Major')
    course.objects.create(CuNo=CuNo, CuName=CuName,).save()
    return render(request, 'teacher/admin_add_course.html', {'is_add': is_add})



def admin_find_course(request):
    CuNo = request.POST.get('CuNo')
    CuName = request.POST.get('CuName')
    is_arrange = 0
    teacher=models.teacher.objects.all()
    if CuNo != '':
        course=models.course.objects.filter(CuNo = CuNo)
        return render(request, 'teacher/admin_arrange_course.html',
                      {'is_arrange': is_arrange, 'course': course, 'teacher': teacher})
    elif CuNo != '':
        course= models.course.objects.filter(CuName_contains=CuName)
        return render(request, 'teacher/admin_arrange_course.html',
                      {'is_arrange': is_arrange, 'course': course, 'teacher': teacher})
    else:
        course = models.course.objects.all()
        return render(request, 'teacher/admin_arrange_course.html',
                      {'is_arrange': is_arrange, 'course': course, 'teacher': teacher})
