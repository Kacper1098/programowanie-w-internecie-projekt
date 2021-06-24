from model_mommy import mommy
from django.contrib.auth import get_user_model
from django.urls import resolve

from backend.tests.viewset_test_base import ViewSetTestBase
from mydentist.models import Visit, Patient, Doctor

User = get_user_model()


class TestVisitViewSetViewset(ViewSetTestBase):
    url_base = "visits-"
    model = Visit
    guest_access = False

    def get_obj(self):
        facility = User.objects.all().first().doctor.facility
        patient = mommy.make(Patient, facility=facility)
        doctor = mommy.make(Doctor, facility=facility)
        return mommy.make(self.model, doctor=doctor, patient=patient)

    def test_update(self, doctor_client):
        if "update" not in self.allowed_actions:
            return

        obj = self.get_obj()
        url = self.get_detail_url(obj)
        serializer = resolve(url).func.cls.serializer_class
        payload = serializer(obj).data
        payload["patient_id"] = payload["patient"]["id"]
        payload["doctor_id"] = payload["doctor"]["id"]
        response = doctor_client.put(url, payload)
        assert response.status_code == 200
        assert self.model.objects.count() == 1

    @property
    def payload(self):
        facility = User.objects.all().first().doctor.facility
        patient = mommy.make(Patient, facility=facility)
        doctor = mommy.make(Doctor, facility=facility)
        return {
            "date": "2020-01-01",
            "start_time": "08:00",
            "end_time": "08:30",
            "patient_id": patient.id,
            "doctor_id": doctor.id,
        }
