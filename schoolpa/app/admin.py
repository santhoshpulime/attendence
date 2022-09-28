from django.contrib import admin
from .models import student,classroom,attendance
admin.site.register(student)
admin.site.register(classroom)
admin.site.register(attendance)