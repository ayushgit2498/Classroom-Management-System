from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    bdate = models.CharField(max_length=44)
    phone = models.CharField(max_length=10)
    rno = models.IntegerField(default=0, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


# Create your models here.
class Test(models.Model):
    subject = models.CharField(max_length=44)
    date = models.DateField()
    desc = models.CharField(max_length=85)
    tm = models.IntegerField(default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject + " " + self.desc


class TestRecord(models.Model):
    stu = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    marks = models.IntegerField(default=0)
    rks = models.CharField(max_length=44)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test')

    def __str__(self):
        return str(self.stu) + " " + str(self.marks)


class Attendance(models.Model):
    date = models.DateField()
    stu = models.ForeignKey(Student, on_delete=models.CASCADE)


class Notice(models.Model):
    date = models.DateField()
    notice = models.CharField(max_length=300)

    def __str__(self):
        return str(self.date)


class TimeTable(models.Model):
    date = models.DateField()
    subject = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    topic = models.CharField(max_length=50)
