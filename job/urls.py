from django.urls import path

from . import views

app_name = 'job'


urlpatterns=[
    # path('', views.Index.as_view(), name='index'),

    # 不需要token的api
    path('login/', views.login.as_view(), name='login'),
    # 需要token的api
    # path('manager/homepage/', views.manager_homepage.as_view(), name=''),
    # path('manager/', views..as_view(), name='')
    # path('manager/', views..as_view(), name='')

    path('teacher/homepage/', views.teacher_homepage.as_view()),
    path('student/homepage/', views.student_homepage.as_view()),

]



# #path('homework/', views.homework.as_view(), name='homework'),
# path('homework_publish/', views.homework_publish, name='homework_publish'),