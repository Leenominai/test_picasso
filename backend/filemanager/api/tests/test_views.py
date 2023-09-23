import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from files.models import File
from api.serializers import FileSerializer
from api.tasks import process_uploaded_file
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db(transaction=True)
class FileListViewTestCase(TestCase):
    """
    Тесты для API-вьюсета FileListView.

    Этот класс содержит тесты для методов API-вьюсета, отвечающего за создание и получение списка файлов.
    """

    def setUp(self):
        self.client = APIClient()

    def test_list_files(self):
        """
        Тест получения списка файлов.

        Этот тест выполняет следующие действия:
        1. Создает несколько файлов.
        2. Отправляет GET-запрос для получения списка файлов.
        3. Проверяет статус ответа и корректность данных.
        """
        file1 = File.objects.create(file="file1.txt")
        file2 = File.objects.create(file="file2.txt")

        response = self.client.get(reverse("file-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [
            FileSerializer(file1).data,
            FileSerializer(file2).data,
        ]
        self.assertEqual(response.data, expected_data)


@pytest.mark.django_db(transaction=True)
class FileDetailViewTestCase(TestCase):
    """
    Тесты для API-вьюсета FileDetailView.

    Этот класс содержит тесты для методов API-вьюсета, отвечающего за получение деталей, обновление и удаление файлов.
    """

    def setUp(self):
        self.client = APIClient()
        self.file = File.objects.create(file="test.txt")

    def test_retrieve_file(self):
        """
        Тест получения деталей файла.

        Этот тест выполняет следующие действия:
        1. Отправляет GET-запрос для получения деталей файла.
        2. Проверяет статус ответа и корректность данных.
        """
        response = self.client.get(reverse("file-detail", args=[self.file.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = FileSerializer(self.file).data
        self.assertEqual(response.data, expected_data)

    def test_update_file(self):
        """
        Тест обновления файла.

        Этот тест выполняет следующие действия:
        1. Создает временный файл для обновления.
        2. Отправляет PUT-запрос для обновления файла.
        3. Проверяет статус ответа и обновление файла в базе данных.
        """

        updated_file_content = b'This is updated file content.'
        updated_file = SimpleUploadedFile("updated_file.txt", updated_file_content)

        response = self.client.put(
            reverse("file-detail", args=[self.file.id]),
            {"file": updated_file},
            format="multipart"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.file.refresh_from_db()

        # Проверьте, что имя файла соответствует обновленному файлу
        self.assertEqual(self.file.file.name, updated_file.name)

    def test_delete_file(self):
        """
        Тест удаления файла.

        Этот тест выполняет следующие действия:
        1. Отправляет DELETE-запрос для удаления файла.
        2. Проверяет статус ответа и удаление файла из базы данных.
        """
        response = self.client.delete(reverse("file-detail", args=[self.file.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(File.objects.filter(pk=self.file.id).exists())


@pytest.mark.django_db(transaction=True)
class FileUploadViewTestCase(TestCase):
    """
    Тесты для API-вьюсета FileUploadView.

    Этот класс содержит тесты для метода API-вьюсета, отвечающего за загрузку файлов.
    """
    def setUp(self):
        self.client = APIClient()

    def test_upload_files(self):
        """
        Тест загрузки файлов.

        Этот тест выполняет следующие действия:
        1. Создает временные файлы для загрузки.
        2. Отправляет POST-запрос для загрузки файлов.
        3. Проверяет статус ответа и корректность данных.
        """
        file_content1 = b'This is file 1 content.'
        file_content2 = b'This is file 2 content.'
        uploaded_file1 = SimpleUploadedFile("file1.txt", file_content1)
        uploaded_file2 = SimpleUploadedFile("file2.txt", file_content2)

        response = self.client.post(reverse("file-upload"),
                                    {"file": [uploaded_file1, uploaded_file2]}, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(isinstance(response.data, list))
        self.assertEqual(len(response.data), 2)
