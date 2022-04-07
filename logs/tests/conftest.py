import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

EMAIL = "Test@test.ru"
PASSWORD = "TestTestTest"


@pytest.fixture
def user():
    user = User.objects.create_user(
        username=EMAIL,
        email=EMAIL,
    )
    user.set_password(PASSWORD)
    user.save()
    return user


@pytest.fixture
def guest_client():
    client = APIClient()
    return client


@pytest.fixture
def authorized_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client
