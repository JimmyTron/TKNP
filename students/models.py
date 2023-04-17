from django.db import models
from django.contrib.auth.models import User
from clearance.models import Department, Course
from PIL import Image 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Adm_no =models.CharField(max_length=100)


    def __str__(self):
        return f'{self.user.username} Profile'

class Student(models.Model):
    adm_no = models.CharField(max_length=100)  
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.adm_no