"""jobsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('add_student/', views.add_student),
    #path('add_teacher/', views.add_teacher),
    #path('add_course/', views.add_course),
    #path('admin_find_course/', views.admin_find_course),
    #path('add_notice/', views.add_notice),
    #path('is_admin/', views.is_admin),
    # path('manager_login/', views.manager_login),
    # path('teacher_login/', views.teacher_login),
    # path('student_login/', views.student_login),
    # #path('teacher_homepage/', views.teacher_homepage),
    # #path('homework/', views.homework.as_view(), name='homework'),
    # path('homework_publish/', views.homework_publish, name='homework_publish'),
]

# path('course_function/', views.course_function),
# path('sign/', views.sign),
# path('homework_list/', views.homework_list),
# path('homework_score/', views.homework_score),
# path('student_homepage/', views.student_mainpage),
# path('student_course/', views.student_course),
# path('student_homework/', views.student_homework),
# path('student_sign/', views.student_sign),
# path('student_finish/', views.student_finish),
# path('student_check/', views.student_check),
# path('logout/', views.logout),
