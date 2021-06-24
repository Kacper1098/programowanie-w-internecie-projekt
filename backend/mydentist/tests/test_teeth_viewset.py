from model_mommy import mommy
from django.contrib.auth import get_user_model

from backend.tests.viewset_test_base import ViewSetTestBase
from mydentist.models import Patient, Tooth

User = get_user_model()


class TestTeethViewSetViewset(ViewSetTestBase):
    url_base = "teeth-"
    model = Tooth
    guest_access = False
    facility = None

    def get_obj(self):
        facility = User.objects.all().first().doctor.facility
        patient = mommy.make(Patient, facility=facility)
        return mommy.make(self.model, patient=patient)

    @property
    def payload(self):
        facility = User.objects.all().first().doctor.facility
        patient = mommy.make(Patient, facility=facility)
        return {
            "number": 1,
            "horizontally": Tooth.Horizontally.top,
            "vertically": Tooth.Vertically.right,
            "note": "Notatka",
            "patient": patient.id
        }
