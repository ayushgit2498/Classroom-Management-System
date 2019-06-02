from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Test)
admin.site.register(TestRecord)
admin.site.register(Attendance)
admin.site.register(TimeTable)
admin.site.register(Notice)
