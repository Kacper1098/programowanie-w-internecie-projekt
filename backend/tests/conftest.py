import pytest

from django.test import Client
from django.test.client import MULTIPART_CONTENT
from mydentist.models import Doctor, Facility


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


class DefaultJSONClient(Client):
    def multipart_post(
        self, path, data=None, content_type=MULTIPART_CONTENT, secure=False, **extra
    ):
        """Construct a POST request."""
        data = self._encode_json({} if data is None else data, content_type)
        post_data = self._encode_data(data, content_type)

        return self.generic(
            "POST", path, post_data, content_type, secure=secure, **extra
        )

    def post(
        self,
        path,
        data=None,
        content_type="application/json",
        follow=False,
        secure=False,
        **extra
    ):
        return super().post(path, data, content_type, follow, secure, **extra)

    def put(
        self,
        path,
        data="",
        content_type="application/json",
        follow=False,
        secure=False,
        **extra
    ):
        """Send a resource to the server using PUT."""
        return super().put(
            path, data=data, content_type=content_type, secure=secure, **extra
        )

    def patch(
        self,
        path,
        data="",
        content_type="application/json",
        follow=False,
        secure=False,
        **extra
    ):
        """Send a resource to the server using PATCH."""
        response = super().patch(
            path, data=data, content_type=content_type, secure=secure, **extra
        )
        if follow:
            response = self._handle_redirects(
                response, data=data, content_type=content_type, **extra
            )
        return response


@pytest.fixture
def client():
    return DefaultJSONClient()


@pytest.fixture()
def doctor_user(db, django_user_model, django_username_field):
    UserModel = django_user_model
    username_field = django_username_field
    username = "doctor@example.com" if username_field == "email" else "doctor"

    try:
        user = UserModel._default_manager.get(**{username_field: username})
    except UserModel.DoesNotExist:


        user = UserModel._default_manager.create_superuser("doctor", "password")
        user.set_password("password")
        user.save()
        facility = Facility.objects.create(name="Testowa Placowka")
        Doctor.objects.update_or_create(name="Jan", surname="Doc", pwz="123", facility=facility, user=user)
    return user


@pytest.fixture()
def doctor_client(doctor_user):
    client = DefaultJSONClient()
    client.login(username=doctor_user.username, password="password")
    return client


