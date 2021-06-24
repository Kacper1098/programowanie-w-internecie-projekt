import os

from django.dispatch import receiver
from django.db.models.signals import post_save


from mydentist.functions import send_verification_email
from mydentist.models import Doctor


@receiver(post_save, sender=Doctor)
def doctor_post_save(sender, **kwargs):
    if kwargs['created']:
        doctor = kwargs['instance']
        if not doctor.user.is_active:
            send_verification_email(doctor.id)

