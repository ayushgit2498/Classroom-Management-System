"""DBMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from sms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.testRecord),
    path('addTestRecords/<int:numR>/', views.addTestMarks),
    path('addtestrecords/<int:number>/', views.addTest),
    path('attendance/', views.attendance),
    path('aft/', views.aft),
    path('notice/', views.notice, name='notice'),
    path('absent/', views.absent, name='absent'),
    path('profile/', views.profile, name='profile'),
    path('profilep/', views.profilep, name='profilep'),
    path('testList/', views.aftList),
    path('timetable/', views.timetable),
    path('teststudent/', views.tests),
    path('performance/', views.performance),
    path('addnotice/', views.addnotice),
    path('addtimetable/', views.addtimetable),
    path('dummy/', views.dummy),
    path('testrank/', views.testrank),
    path('testList/', views.aftList),
    path('', views.loginfunc),
    path('logout/', views.logoutfunc)
]
