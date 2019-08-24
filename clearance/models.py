from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Request(models.Model):
    request = models.CharField(default="Clearance Request", max_length=100)
    content = models.TextField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.request

class Department(models.Model):
    department = models.CharField(max_length=100)
    hod = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.department

class Course(models.Model):
    course = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.course 

class Subject(models.Model):
    subject = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject