import pytest
import tempfile
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
        with tempfile.NamedTemporaryFile() as tmp_file:
            tmp_file.write(b'This is a test file content.')
            tmp_file.seek(0)
            uploaded_file = SimpleUploadedFile("example.txt", tmp_file.read())

        file = File.objects.create(file=uploaded_file)

        serializer = FileSerializer(file)

        self.assertTrue(serializer.is_valid())

        expected_fields = ["file", "uploaded_at", "processed"]
        for field in expected_fields:
            self.assertIn(field, serializer.data)

        self.assertTrue(serializer.data["file"].startswith("/"))
        self.assertNotIn("/media/", serializer.data["file"])
