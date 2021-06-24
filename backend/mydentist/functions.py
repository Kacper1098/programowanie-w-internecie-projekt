import os

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponseRedirect
from django.template import loader

from dentist.settings import BASE_DIR, BASE_URL_FRONTEND
from mydentist.models import Doctor, Tooth
UserModel = get_user_model()


def send_verification_email(doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)

    subject = 'Potwierdz konto MyDentist'
    message = 'Aktywuj konto pod tym linkiem: ' + \
              'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(doctor.verification_uuid)})
    from_email = 'support@mydentist.com'
    to_email = [doctor.user.email]
    path = os.path.join(BASE_DIR, 'templates/activation_email.html')
    html_message = loader.render_to_string(path, {
        'user_name': doctor.name or '',
        'verification_code': 'http://localhost:8000%s' % reverse('verify',
                                                                 kwargs={'uuid': str(doctor.verification_uuid)})
    })
    send_mail(subject, message, from_email, to_email, fail_silently=False, html_message=html_message)


def verify(request, uuid):
    try:
        doctor = Doctor.objects.get(verification_uuid=uuid, user__is_active=False)
    except Doctor.DoesNotExist:
        raise Http404("Użytkownik nie istnieje lub jest juz aktywny")

    user = doctor.user
    user.is_active = True
    user.save()

    return HttpResponseRedirect(BASE_URL_FRONTEND + '/#/email-confirm')


def create_patient_teeth(patient_id):
    for i in range(1, 9):
        Tooth.objects.get_or_create(patient_id=patient_id, number=i,
                                    horizontally=Tooth.Horizontally.top, vertically=Tooth.Vertically.left)
        Tooth.objects.get_or_create(patient_id=patient_id, number=i,
                                    horizontally=Tooth.Horizontally.bottom, vertically=Tooth.Vertically.left)
        Tooth.objects.get_or_create(patient_id=patient_id, number=i,
                                    horizontally=Tooth.Horizontally.top, vertically=Tooth.Vertically.right)
        Tooth.objects.get_or_create(patient_id=patient_id, number=i,
                                    horizontally=Tooth.Horizontally.bottom, vertically=Tooth.Vertically.right)


