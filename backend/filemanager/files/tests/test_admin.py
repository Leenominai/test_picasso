from django.test import TestCase
from django.urls import reverse
from django.test import Client
from rest_framework import status
from files.models import File, TextDocument


class AdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.file = File.objects.create(file='test_file.txt')

    def test_admin_file_list_view(self):
        """
        Проверяет, что административное представление списка файлов возвращает статус 200 (OK).
        """
        url = reverse("admin:files_file_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_admin_file_change_view(self):
        """
        Проверяет, что административное представление изменения файла возвращает статус 200 (OK).
        """
        url = reverse("admin:files_file_change", args=[self.file.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_admin_file_add_view(self):
        """
        Проверяет, что административное представление добавления файла возвращает статус 200 (OK).
        """
        url = reverse("admin:files_file_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_admin_file_search(self):
        """
        Проверяет, что поиск файла в административном представлении возвращает результаты с файлом "test.txt".
        """
        url = reverse("admin:files_file_changelist")
        response = self.client.get(url, {"q": "test"})
        content = response.content.decode("utf-8")
        self.assertIn(self.file.file.name, content)
