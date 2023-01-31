from django.contrib import admin
from django.db.models import signals
from django.dispatch import receiver
from .models import (Request, Department, Course, Subject, Notification)


class NotificationAdmin(admin.ModelAdmin):
   @receiver(signals.post_save, sender=Request)
   def create_notification(sender, instance, created, **kwargs):

    if created:
        for department in instance.departments.all():
            Notification.objects.create(title=instance.student, description=[instance.status,instance.date_posted], department=department)
        

admin.site.register(Request)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Notification,NotificationAdmin)
