from model_mommy import mommy
from django.urls import reverse
from mydentist.models import Doctor


def test_doctor_only_from_facility(doctor_client):
    mommy.make(Doctor, _quantity=2)
    url = reverse("doctors-list")
    response = doctor_client.get(url)
    data = response.data
    assert data
    assert Doctor.objects.count() == 3
    assert len(data) == 1