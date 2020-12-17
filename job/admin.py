from django.contrib import admin
from .models import token, student, manager, notice, teacher, course, homework, question, sign

admin.site.register(token)
admin.site.register(student)
admin.site.register(manager)
admin.site.register(notice)
admin.site.register(teacher)
admin.site.register(course)
admin.site.register(homework)
admin.site.register(question)
admin.site.register(sign)


