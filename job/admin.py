from django.contrib import admin
from .models import sign, teacher, student, course

admin.site.register(sign)
admin.site.register(teacher)
admin.site.register(student)
admin.site.register(course)