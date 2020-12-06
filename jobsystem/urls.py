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
    path('login/', views.login),
    #path('teacher_homepage/', views.teacher_homepage),
]

'''path('course_function/', views.course_function),
path('sign/', views.sign),
path('homework/', views.homework),
path('homework_publish/', views.homework_publish),
path('homework_list/', views.homework_list),
path('homework_score/', views.homework_score),
path('student_homepage/', views.student_mainpage),
path('student_course/', views.student_course),
path('student_homework/', views.student_homework),
path('student_sign/', views.student_sign),
path('student_finish/', views.student_finish),
path('student_check/', views.student_check),
path('logout/', views.logout),'''