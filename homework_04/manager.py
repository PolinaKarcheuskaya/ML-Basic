"""
Управление файлами 
"""

from .media import MediaFile
from .storage import Storage


class MediaFileManager:

    def __init__(self, storage: Storage) -> None:
        self._storage = storage

    def save(self, media_file: MediaFile) -> None:
        """
        Сохранить файл в хранилище
        """
        path = media_file.path
        self._storage.save(path, media_file)

    def read(self, identifier: str) -> MediaFile:
        """
        Прочитать/загрузить файл по идентификатору.
        """
        raise NotImplementedError("")

    def delete(self, identifier: str) -> None:
        """
        Удалить файл по идентификатору.
        """
        self._storage.delete(identifier)
