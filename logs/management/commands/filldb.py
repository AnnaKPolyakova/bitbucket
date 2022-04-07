from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandError

from logs.tests.factories import UserFactory


def notification(command, objects, text):
    command.stdout.write(
        command.style.SUCCESS(f"{len(objects)} {text} успешно создано.")
    )


class Command(BaseCommand):
    help = (
        "Заполняет БД тестовыми данными. Сейчас доступны:"
        " - Теги,"
        " - Коды,"
        " - Клиенты"
    )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        try:
            user = UserFactory(username="admin", email="admin@admin.ru")
            notification(
                self, [user], (
                    "администратор с username admin и паролем admin"
                )
            )

        except CommandError:
            self.stdout.write(self.style.ERROR("Ошибка наполнения БД"))
