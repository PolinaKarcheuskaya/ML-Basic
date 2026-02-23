"""
Классы для работы с файлами
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


class MediaFile(ABC):
    """
    Абстрактный класс медиа файла
    """

    def __init__(
        self,
        name: str,
        size: int,
        created_at: datetime,
        owner: str,
        path: str,
    ) -> None:
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner
        self.path = path

    @abstractmethod
    def get_metadata(self) -> dict[str, Any]:
        """Возвращает метаданные файла."""
        pass

    def convert(self, new_format: str) -> "MediaFile":
        raise NotImplementedError("Метод конвертации")


class AudioFile(MediaFile):
    """Файл аудио"""
    def __init__(
        self,
        name: str,
        size: int,
        created_at: datetime,
        owner: str,
        duration_sec: float,
        path: str,
    ) -> None:
        super().__init__(name=name, size=size, created_at=created_at, owner=owner, path=path)
        self.duration_sec = duration_sec

    def get_metadata(self) -> dict[str, Any]:
        return {
            "duration_sec": self.duration_sec
        }


class VideoFile(MediaFile):
    """Файл видео"""

    def __init__(
        self,
        name: str,
        size: int,
        created_at: datetime,
        owner: str,
        duration_sec: float,
        resolution: str,
        path: str,
    ) -> None:
        super().__init__(name=name, size=size, created_at=created_at, owner=owner, path=path)
        self.duration_sec = duration_sec
        self.resolution = resolution

    def get_metadata(self) -> dict[str, Any]:
        return {
            "duration_sec": self.duration_sec,
            "resolution": self.resolution
        }
