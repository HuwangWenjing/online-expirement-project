from django.contrib import admin

from job.models import *

class StudentAdmin(admin.ModelAdmin):
    fields=('StuNo', 'StuName',"StuSex","Major")
    list_display = ['StuNo', 'StuName',
                    ]

class TeacherAdmin(admin.ModelAdmin):
    fields = ('TeaNo', 'TeaName', "TeaSex")
    list_display = ['TeaNo', 'TeaName',
                    'TeaSex'
                    ]

class CourseAdmin(admin.ModelAdmin):
    fields = ('CuNo', 'CuName', "TeaNo")
    list_display = ['CuNo', 'CuName'
                    ]


class NoticeAdmin(admin.ModelAdmin):
    fields = ('NoticeTitle', 'NoticePubTime', "NoticeContent","MaNo")
    list_display = ['NoticeNo','NoticeTitle', 'NoticeContent', 'NoticePubTime']



admin.site.register(student,StudentAdmin)
admin.site.register(teacher, TeacherAdmin)
admin.site.register(course, CourseAdmin)
admin.site.register(notice, NoticeAdmin)
#admin.site.register(sign)
