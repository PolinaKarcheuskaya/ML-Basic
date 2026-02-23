"""
Абстракция управления хранением файлов.
Абстрактный класс задает методы для работы с хранилищами, а классы наследники реализуют эти методы
"""

from abc import ABC, abstractmethod
from typing import Any


class Storage(ABC):

    @abstractmethod
    def save(self, path: str, data: Any) -> None:
        pass

    @abstractmethod
    def read(self, identifier: str) -> Any:
        pass

    @abstractmethod
    def delete(self, identifier: str) -> None:
        pass


class LocalStorage(Storage):
    """
    Класс реализующий методы для работы с локальным хранилищем. 
    """

    def __init__(self, directory: str) -> None:
        self.directory = directory

    def save(self, path: str, data: Any) -> None:
        pass

    def read(self, identifier: str) -> Any:
        pass

    def delete(self, identifier: str) -> None:
        pass

    def exist(self, identifier: str) -> bool:
        return False


class RemoteStorage(Storage):
    """
    Класс для работы с удаленным хранилищем
    """

    def __init__(self, url: str) -> None:
        self.url = url

    def save(self, path: str, data: Any) -> None:
        pass

    def read(self, identifier: str) -> Any:
        pass

    def delete(self, identifier: str) -> None:
        pass

    def get_count(self) -> int:
        return 0
