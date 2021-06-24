from model_mommy import mommy
from django.contrib.auth import get_user_model

from backend.tests.viewset_test_base import ViewSetTestBase
from mydentist.models import Patient, Facility

User = get_user_model()


class TestPatientViewSetViewset(ViewSetTestBase):
    url_base = "patients-"
    model = Patient
    guest_access = False
    facility = None

    def get_obj(self):
        facility = User.objects.all().first().doctor.facility
        return mommy.make(self.model, facility=facility)

    @property
    def payload(self):
        facility = User.objects.all().first().doctor.facility

        return {
            "name": "Jacek",
            "surname": "Kowalski",
            "sex": "m",
            "telephone": "123456789",
            "pesel": "99030329345",
            "city": "Miasto",
            "street": "Ulica 3",
            "postal_code": "11-111",
            "country": "Polska",
            "facility": facility.id,
        }
