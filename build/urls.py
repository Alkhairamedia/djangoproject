from django.contrib import admin
from django.urls import path


from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.loginpage, name = 'loginpage'),
    path('logout/', views.logoutuser, name = 'logout'),
    
    path('teacher/<str:pk_test>/', views.dashboard_teacher, name = 'teacher'),
    
    path('staff/', views.dashboard_staffs, name = 'staff'),
    
    path('parent/', views.dashboard_parents, name = 'parent'),
    
    path('schemeOfWork/', views.schemeOfWork, name = 'schemeOfWork'),
    
    path('studentResult/', views.studentResult, name = 'studentResult'),
    
    path('parentResult/', views.parentResult, name = 'parentResult'),
    
    path('teacherResult/', views.teacherResult, name = 'teacherResult'),
    
    path('student/', views.dashboard_students, name = 'student'),    

    path('teacherforum/', views.teacherforum, name = 'teacherforum'),
    
    path('studentforum/', views.studentforum, name = 'studentforum'),
    
    path('assignment/', views.assignment, name = 'assignment'),
    
    path('parentforum/', views.parentforum, name = 'parentforum'),
    
    path('about/', views.about, name = 'about'),
    path('news/', views.news, name = 'news'),
    path('beststudents/', views.beststudents, name = 'beststudents'),
]