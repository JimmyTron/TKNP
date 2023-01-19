from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Department(models.Model):
    department = models.CharField(max_length=100)
    hod = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.department

class Request(models.Model):
    STATUS = (
    (0,"Pending"),
    (1,"Cleared"),
    (2,"Declined")
     )
    request = models.CharField(default="Clearance Request", max_length=100)
    departments = models.ManyToManyField(Department)
    date_posted = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0) 

    def __str__(self):
        #return f'{self.student.profile.Adm_no, self.student.first_name, self.request}'
        return self.student.first_name +" "+ self.student.last_name+" "+ self.student.profile.Adm_no +" "+ self.request

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