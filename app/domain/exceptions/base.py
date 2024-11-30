from dataclasses import dataclass


@dataclass(eq=True)
class ApplicationException(Exception):
    """Базовая ошибка приложения"""
    @property
    def message(self):
        return 'Произошла ошибка приложения'
