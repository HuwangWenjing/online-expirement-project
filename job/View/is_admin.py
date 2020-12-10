from django.shortcuts import render

from job.models import *
def is_admin(request):
    '''管理员判定'''
    password = request.POST.get('password')
    if password == 'abc12345678':
        return render(request, 'teacher/admin_index.html')
    else:
        error = True
        return render(request, 'teacher/admin.html', {'error': error})
