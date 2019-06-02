from django.shortcuts import render
import datetime
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
# Create your views here.

def testRecord(request):
    context = {
        'fname': request.user.first_name,
        'lname': request.user.last_name,
    }
    return render(request, "testrecords.html", context)


def addTest(request, number):
    out = ""
    for x in range(number):
        out += str(x)
    context = {
        'fname': request.user.first_name,
        'lname': request.user.last_name,
        'i': out,
        'number': number
    }
    return render(request, "addtestrecords.html", context)


def addTestMarks(request, numR):
    subject = request.POST["sub"]
    datet = request.POST["dateT"]
    tmarks = request.POST["tmarks"]
    desc = request.POST["description"]
    tea = Teacher.objects.get(id=1)
    test = Test.objects.create(subject=subject, date=datet, desc=desc, tm=tmarks, teacher=tea)
    for i in range(numR):
        sid = request.POST["studentID" + str(i)]
        om = request.POST["obtainedmarks" + str(i)]
        rmks = request.POST["remarks" + str(i)]
        stu = Student.objects.get(rno=sid)
        test2 = TestRecord.objects.create(stu=stu, marks=om, test=test, rks=rmks)
        print(test)

    context = {
        'fname': request.user.first_name,
        'lname': request.user.last_name,
        'snackBar': True,
        'snackBarStyle': 'hsdone',
        'SnackBarText': 'Test Data added Successfully'
    }
    return render(request, "testrecords.html", context)


def attendance(request):
    if request.method == "GET":
        m = Student.objects.all()
        print(m)
        context = {
            'fname': request.user.first_name,
            'lname': request.user.last_name,
            'student': m
        }
        return render(request, "Attendance.html", context)
    else:
        m = Student.objects.all()
        dateT = request.POST["dateT"]
        for i in m:
            ap = request.POST.get("ap" + str(i.rno))
            if not ap:
                attend = Attendance.objects.create(date=dateT, stu=i)
        context = {
            'fname': request.user.first_name,
            'lname': request.user.last_name,
            'snackBar': True,
            'snackBarStyle': 'hsdone',
            'SnackBarText': 'Test Data added Successfully'
        }
        return render(request, "testrecords.html", context)
def aft(request):
    if request.method == "GET":
        context = {
            'fname': request.user.first_name,
            'lname': request.user.last_name,
        }
        return render(request, "aft.html", context)
    else:
        subject = request.POST["sub"]
        datet = request.POST["dateT"]
        tmarks = request.POST["tmarks"]
        desc = request.POST["description"]
        tea = Teacher.objects.get(id=1)
        test = Test.objects.create(subject=subject, date=datet, desc=desc, tm=tmarks, teacher=tea)
        context = {
            'fname': request.user.first_name,
            'lname': request.user.last_name,
            'snackBar': True,
            'snackBarStyle': 'hsdone',
            'SnackBarText': 'New Test Data added Successfully'
        }
        return render(request, "testrecords.html", context)


def aftList(request):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(days=6)
    test = Test.objects.all()
    context = {
        'fname': request.user.first_name,
        'lname': request.user.last_name,
        'test': test
    }
    return render(request, "testlist.html", context)


def loginfunc(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        u2 = authenticate(request, username=username, password=password)
        if u2:
            login(request, u2)
            return HttpResponseRedirect("/test")
        else:
            context = {
                'error': 'wrong user name Password'
            }
            return render(request, "login.html", context)


def logoutfunc(request):
    logout(request)

    return HttpResponseRedirect("/")

def login1(request):

    return 0

def absent(request):
    c = Student.objects.get(rno=3225)
    arecords = Attendance.objects.filter(stu=c)
    #
    return render(request, 'absent.html', {'records': arecords})

def notice(request):
    print("*" * 60 + "outsidepost")
    if request.method == 'POST':
        print("*" * 40)
        date1 = request.POST['dateT']
        notice1 = request.POST['notice']

        c = Notice.objects.create(date=date1, notice=notice1)
        arecords = Notice.objects.all()
        return render(request, 'notice.html', {'records': arecords})
    else:
        arecords = Notice.objects.all()
        return render(request, 'notice.html', {'records': arecords})

def profile(request):

    return render(request, 'profilestudent.html', {})

def profilep(request):

    return render(request, 'parentprofile.html', {})


def timetable(request):
    if request.method == 'POST':
        date = request.POST['dateT']
        subject = request.POST['subject']
        topic = request.POST['topic']
        time = request.POST['time']

        n1 = TimeTable.objects.create(date=date, subject=subject, topic=topic, time=time)
        trecords = TimeTable.objects.all()
        return render(request, 'timetable.html', {'trecords': trecords})
    else:
        trecords = TimeTable.objects.all()
        return render(request, 'timetable.html', {'trecords': trecords})


def tests(request):
    trecords = Test.objects.all()
    return render(request, 'tests.html', {'trecords': trecords})


def performance(request):
    if request.method == 'POST':
        print("inside")
        subject = request.POST['subject1']
        test1 = Test.objects.filter(subject=subject)
        print(test1, end='\n')
        c = Student.objects.get(rno=3225)
        strecords = []
        for testf in test1:
            strecords.extend(TestRecord.objects.filter(test=testf).filter(stu=c))
        context = {'records': strecords}
        return render(request, 'performance.html', context)

    return render(request, 'performance.html', {})


def addnotice(request):
    return render(request, 'addnotice.html', {})


def addtimetable(request):
    return render(request, 'addtimetable.html', {})


def dummy(request):
    if request.method == 'POST':
        subject = request.POST['subject1']
        dates = Test.objects.filter(subject=subject)
        return render(request, 'testrank.html', {'subject': subject, 'dates': dates, 'check': 0})
    else:
        return render(request, 'dummy.html', {})


def testrank(request):
    if request.method == 'POST':
        subject = request.POST['subject1']
        date = str(request.POST['date'])
        import dateparser
        c = str(dateparser.parse(date))
        l = c.split(' ')
        print(date + " thisone")
        print(l[0])
        test = Test.objects.get(subject=subject, date=l[0])
        records = TestRecord.objects.filter(test=test).order_by('marks').reverse()
        c = Student.objects.get(rno=3225)
        print(c)
        sturecord = TestRecord.objects.filter(test=test).filter(stu=c)
        print(sturecord)
        context = {'records': records, 'subject': subject, 'date': date, 'check': 1, 'record1': sturecord}
        return render(request, 'testrank.html', context)
