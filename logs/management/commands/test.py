from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandError

from logs.utils import parsing_logs


class Command(BaseCommand):
    help = (
        "Заполняет БД тестовыми данными. Сейчас доступны:"
        " - Теги,"
        " - Коды,"
        " - Клиенты"
    )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        try:
            parsing_logs()
            pass

        except CommandError:
            self.stdout.write(self.style.ERROR("Ошибка наполнения БД"))