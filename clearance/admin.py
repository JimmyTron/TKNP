from django.contrib import admin
from .models import (Request, Department, Course, Course_Subject)

admin.site.register(Request)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Course_Subject)
