from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Staffs)
admin.site.register(Students)
admin.site.register(subjects)
admin.site.register(Parents)
admin.site.register(attendance)
admin.site.register(department)
admin.site.register(scheme_of_work)
admin.site.register(teachers)
