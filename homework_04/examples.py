"""
Примеры использования
"""

from datetime import datetime

from .media import AudioFile, MediaFile, VideoFile
from .manager import MediaFileManager
from .storage import LocalStorage, RemoteStorage


def create_examples():
    """Создание экземпляров медиа-файлов."""
    now = datetime.now()
    audio = AudioFile(
        name="track.mp3",
        size=4_000_000,
        created_at=now,
        owner="user1",
        duration_sec=180.5,
        path="/media/track.mp3",
    )
    video = VideoFile(
        name="clip.mp4",
        size=50_000_000,
        created_at=now,
        owner="user1",
        duration_sec=120.0,
        resolution="1920x1080",
        path="/media/clip.mp4",
    )
    return audio, video


def update_example(manager, media_file):
    """Обновление: меняем поля и сохраняем через менеджер."""
    media_file.owner = "user2"
    media_file.name = "renamed_" + media_file.name
    manager.save(media_file)


def delete_example(manager, identifier):
    """Удаление файла по идентификатору."""
    manager.delete(identifier)


def local_storage_example():
    """Работа с локальным хранилищем."""
    storage = LocalStorage("/tmp/media")
    manager = MediaFileManager(storage)
    audio, video = create_examples()
    manager.save(audio)
    manager.save(video)


def remote_storage_example():
    """Работа с удалённым хранилищем"""
    storage = RemoteStorage("https://test-url.com")
    manager = MediaFileManager(storage)
    audio, _ = create_examples()
    manager.save(audio)
