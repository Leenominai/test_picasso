import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from files.models import File


@pytest.mark.django_db(transaction=True)
class URLTestCase(TestCase):
    def test_file_list_url(self):
        """
        Проверяет, что URL для списка файлов возвращает статус 200 (OK).
        """
        url = reverse("file-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_file_detail_url(self):
        """
        Проверяет, что URL для деталей файла возвращает статус 200 (OK) после создания файла с id=10.
        """
        File.objects.create(id=10, file="test_file.txt")
        url = reverse("file-detail", args=[10])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
