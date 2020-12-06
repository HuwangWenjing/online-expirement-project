from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

def login(request):
    pass
    return render(request, 'job/login.html')

'''def course_index(request):
    pass
    return render(request, 'job/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")'''