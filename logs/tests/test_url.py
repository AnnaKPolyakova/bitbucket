import pytest
from django.urls import reverse

LOGS_URL = reverse("logs-list")

pytestmark = pytest.mark.django_db


class TestClientAPI:

    def test_get_logs_url(self, authorized_client):
        url = LOGS_URL
        status = 200
        response = authorized_client.get(url)
        assert response.status_code == status, (
            f"Проверьте, что при get запросе"
            f"{url} возвращается статус {status}"
        )

    def test_get_logs_url_2(self, guest_client):
        url = LOGS_URL
        status = 403
        response = guest_client.get(url)
        assert response.status_code == status, (
            f"Проверьте, что при get запросе"
            f"{url} возвращается статус {status}"
        )

