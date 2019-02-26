from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student


# Create your views here.
def index(request):
    return render(request, 'student/index.html')


def add(request):
    return render(request, 'student/add.html')

def addhandle(request):
    name=request.POST.get('name')
    age=request.POST.get('age')
    date=request.POST.get('date')
    stu=Student()
    stu.bname=name
    stu.bage=age
    stu.bdate=date
    stu.save()
    return HttpResponse("保存成功")


def delete(request):
    return render(request, 'student/delete.html')

def deletehandle(request):
    name=request.POST.get('name')
    stu=Student.objects.get(bname=name)
    stu.isDelete=1
    stu.save()
    return HttpResponse('删除成功')

def modify(request):
    return render(request, 'student/modify.html')


def check(request):
    return render(request, 'student/check.html')
