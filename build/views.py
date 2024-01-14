from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
from .models import *



def loginpage(request) :
   if request.user.is_authenticated:
      return redirect('teacher/<str:pk_test>/')
   else:
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(request, username=username, password=password)

         if user is not None:
            login(request, user)
            return redirect('teacher/<str:pk_test>/')
         else:
            messages.info(request, 'username or password is incorrect')

      context = {}
      return render(request, 'login.html', context)


def logoutuser(request):
      logout(request)
      return redirect('loginpage')
      


def home(request) :
   return render(request, 'Home.html')


# @login_required(login_url='loginpage')
def dashboard_teacher(request, pk_test) :
   teacher = teachers.objects.get(id=pk_test)
   student = teacher.students_set.all()
   totalStudent = student.count()
   Attendance = attendance.objects.all()
   
   context ={'teacher':teacher, 'student':student, 'Attendance':Attendance, 'totalStudent':totalStudent}
   return render(request, 'dashboard_teacher.html', context)


# @login_required(login_url='loginpage')
def dashboard_staffs(request) :
   return render(request, 'dashboard_staffs.html')


# @login_required(login_url='loginpage')
def dashboard_students(request) :
   return render(request, 'dashboard_students.html')


# @login_required(login_url='loginpage')
def dashboard_parents(request) :
   return render(request, 'dashboard_parents.html')

# @login_required(login_url='loginpage')
def teacherResult(request) :
   return render(request, 'teacher_result.html')

# @login_required(login_url='loginpage')
def studentResult(request) :
   return render(request, 'student_result.html')

# @login_required(login_url='loginpage')
def parentResult(request) :
   return render(request, 'parent_result.html')

# @login_required(login_url='loginpage')
def teacherforum(request) :
   return render(request, 'teacher_forum.html')

# @login_required(login_url='loginpage')
def studentforum(request) :
   return render(request, 'student_forum.html')

# @login_required(login_url='loginpage')
def assignment(request) :
   return render(request, 'assignment.html')

# @login_required(login_url='loginpage')
def parentforum(request) :
   return render(request, 'parent_forum.html')

def schemeOfWork(request) :
   return render(request, 'schemeOfWork.html')

def about(request) :
   return render(request, 'about.html')

def news(request) :
   return render(request, 'news.html')

def beststudents(request) :
   return render(request, 'beststudents.html')
