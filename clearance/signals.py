from django.db.models import signals
from django.dispatch import receiver
from clearance.models import Request

@receiver(signals.post_save, sender=Request)
def create_notification(sender, instance, created, **kwargs):

    if created:
        for department in instance.departments.all():
            Notification.objects.create(title=instance.student, description=[instance.status,instance.date_posted], department=department)