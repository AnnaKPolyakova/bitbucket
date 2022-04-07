import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ["email", "username"]

    password = factory.PostGenerationMethodCall("set_password", "admin")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.LazyAttribute(
        lambda a: "{}.{}".format(
            a.first_name, a.last_name).lower()
    )
    email = factory.LazyAttribute(
        lambda a: "{}.{}@test.com".format(
            a.first_name, a.last_name).lower()
    )
    is_staff = True
    is_superuser = True
