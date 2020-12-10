from django.shortcuts import render

from job.models import *
def add_notice(request):
    '''管理员发布通知'''
    NoticeTitle = request.POST.get('NoticeTitle')
    NoticeContent = request.POST.get('NoticeContent')
    is_add = True
    notice.objects.create(NoticeTitle=NoticeTitle, NoticeContent=NoticeContent)
    return render(request, 'teacher/add_notice.html', {'is_add': is_add})
