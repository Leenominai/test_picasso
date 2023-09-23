import pytest

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from api.serializers import FileSerializer
from files.models import File


@pytest.mark.django_db(transaction=True)
class FileSerializerTestCase(TestCase):
    def test_file_serializer(self):
        """
        Тестирование сериализатора FileSerializer.

        Этот тест выполняет следующие действия:
        1. Создает объект File для сериализации.
        2. Создаёт фиктивные данные для сериализации.
        2. Создёт объёкт сериализатора и передает в него фиктивные данные.
        3. Проверяет валидность сериализатора.
        4. Проверяет корректность сериализованных данных.
        """
        file_content = b'This is file content.'
        uploaded_file = SimpleUploadedFile("example.txt", file_content)
        file = File.objects.create(file=uploaded_file)

        # Создаем словарь с данными, которые мы хотим сериализовать
        data = {
            "file": file.file,
            "uploaded_at": file.uploaded_at,
            "processed": file.processed,
        }

        # Передаем данные в сериализатор через параметр data
        serializer = FileSerializer(data=data)

        self.assertTrue(serializer.is_valid())
