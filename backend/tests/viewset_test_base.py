from django.urls import reverse, resolve
from model_mommy import mommy


class ViewSetTestBase:
    url_base = "api:sample-"
    lookup_field = 'pk'
    model = None

    allowed_actions = {
        "retrieve",
        "delete",
        "create",
        "update",
        "partial_update",
        "list",
    }
    disallowed_status_codes = (404, 405)

    @property
    def payload(self):
        return {}

    def get_obj(self):
        return mommy.make(self.model)

    def get_list_url(self):
        if set(self.allowed_actions).intersection({"list", "create"}):
            return self.get_action_url("list")
        return "/force-404/"

    def get_detail_url(self, obj):
        if set(self.allowed_actions).intersection(
            {"retrieve", "delete", "update", "partial_update"}
        ):
            return self.get_action_url("detail", obj)
        return "/force-404/"

    def get_action_url(self, action, obj=None):
        url = self.url_base + action
        if obj is not None:
            kwargs = {self.lookup_field: getattr(obj, self.lookup_field)}
            return reverse(url, kwargs=kwargs)
        return reverse(url)

    def test_detail(self, doctor_client):
        obj = self.get_obj()
        url = self.get_detail_url(obj)
        response = doctor_client.get(url)

        if "retrieve" in self.allowed_actions:
            assert response.status_code == 200
        else:
            assert response.status_code in self.disallowed_status_codes

    def test_list(self, doctor_client):
        [self.get_obj() for _ in range(2)]
        url = self.get_list_url()

        response = doctor_client.get(url)
        if "list" in self.allowed_actions:
            assert response.status_code == 200
            assert len(response.data) == 2
        else:
            assert response.status_code in self.disallowed_status_codes

    def test_delete(self, doctor_client):
        obj = self.get_obj()
        url = self.get_detail_url(obj)

        response = doctor_client.delete(url)

        if "delete" in self.allowed_actions:
            assert response.status_code == 204
            assert self.model.objects.count() == 0
        else:
            assert response.status_code in self.disallowed_status_codes

    def test_create(self, doctor_client):
        url = self.get_list_url()

        response = doctor_client.post(url, self.payload)

        if "create" in self.allowed_actions:
            assert response.status_code == 201
            assert self.model.objects.count() == 1
        else:
            assert response.status_code in self.disallowed_status_codes

    def test_update(self, doctor_client):
        if "update" not in self.allowed_actions:
            return

        obj = self.get_obj()
        url = self.get_detail_url(obj)
        serializer = resolve(url).func.cls.serializer_class
        payload = serializer(obj).data
        response = doctor_client.put(url, payload)
        print(response.data)
        assert response.status_code == 200
        assert self.model.objects.count() == 1
