from django.core.management.base import BaseCommand
from django_scripts_tracker.core_tracker import tracked_script
from mydentist.models import Patient
from mydentist.functions import create_patient_teeth


class Command(BaseCommand):
    help = 'Create teeth for old patient'

    @tracked_script
    def handle(self, *args, **options):
        for patient in Patient.objects.all():
            create_patient_teeth(patient.id)
        self.stdout.write("Teeth created")
