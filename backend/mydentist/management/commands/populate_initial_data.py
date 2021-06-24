from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_scripts_tracker.core_tracker import tracked_script
from django.contrib.auth import get_user_model
from mydentist.models import Visit, Facility, Doctor, Schedule, Patient

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates initial data in db'

    @tracked_script
    def handle(self, *args, **options):
        u1, _ = User.objects.update_or_create(username="testuser")
        u2, _ = User.objects.update_or_create(username="testuser2")
        u1.set_password("xxxx")
        u2.set_password("xxxx")
        u1.save()
        u2.save()

        f1, _ = Facility.objects.update_or_create(name="Testowa Placowka 1")

        d1, _ = Doctor.objects.update_or_create(name="Jan", surname="Lekarski", pwz="12312322", facility=f1, user=u1)
        d2, _ = Doctor.objects.update_or_create(name="Anna", surname="Doktorska", pwz="12312322", facility=f1,
                                                user=u2)

        hours = [{'start': '10:00', 'end': '10:30'}, {'start': '10:30', 'end': '11:00'},
                 {'start': '11:00', 'end': '11:30'}, {'start': '11:30', 'end': '12:00'},
                 {'start': '12:00', 'end': '12:30'}, {'start': '12:30', 'end': '13:00'},
                 {'start': '13:00', 'end': '13:30'}, {'start': '13:30', 'end': '14:00'},
                 {'start': '14:00', 'end': '14:30'}, {'start': '14:30', 'end': '15:00'}]

        dates = [datetime.today().date(), datetime.today().date() + timedelta(days=1)]  # today and tomorrow

        for date in dates:
            for hour in hours:
                Schedule.objects.update_or_create(date=date, start_time=hour['start'], end_time=hour['end'], doctor=d1)
                Schedule.objects.update_or_create(date=date, start_time=hour['start'], end_time=hour['end'], doctor=d2)

        p1, _ = Patient.objects.update_or_create(name="Janusz", surname="Pacjentowy", pesel="56030312456", facility=f1,
                                                 city="Warszawa", country="Polska", street="Rubinowa 2",
                                                 postal_code="02-123", sex="m")
        p2, _ = Patient.objects.update_or_create(name="Anna", surname="Przychodniak", pesel="90110544523", facility=f1,
                                                 city="Poznań", country="Polska", street="Biedna 14",
                                                 postal_code="08-231", sex="f")
        p3, _ = Patient.objects.update_or_create(name="Robert", surname="Kozioł", pesel="85101162258", facility=f1,
                                                 city="Wrocław", country="Polska", street="Towarowa 54",
                                                 postal_code="05-333", sex="m", second_name="Antoni")

        Visit.objects.update_or_create(patient=p1, start_time=hours[4]['start'], end_time=hours[4]['end'],
                                       date=dates[0], doctor=d1)
        Visit.objects.update_or_create(patient=p2, start_time=hours[6]['start'], end_time=hours[6]['end'],
                                       date=dates[0], doctor=d1)
        Visit.objects.update_or_create(patient=p1, start_time=hours[4]['start'], end_time=hours[4]['end'],
                                       date=dates[1], doctor=d2)
        Visit.objects.update_or_create(patient=p3, start_time=hours[1]['start'], end_time=hours[1]['end'],
                                       date=dates[0], doctor=d1)

        self.stdout.write("Initial objects created")
