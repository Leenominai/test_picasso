import pytest
from django.test import TestCase
from files.models import File, TextDocument


@pytest.mark.django_db(transaction=True)
class FileModelTestCase(TestCase):
    def setUp(self):
        self.file = File.objects.create(file="test_file.txt")

    def test_file_creation(self):
        """
        Тестирование создания объекта File.
        """
        self.assertEqual(self.file.__str__(), "test_file.txt")
        self.assertFalse(self.file.processed)


class TextDocumentModelTestCase(TestCase):
    def setUp(self):
        self.document = TextDocument.objects.create(title="Test Document", content="This is a test document.")

    def test_document_creation(self):
        """
        Тестирование создания объекта TextDocument.
        """
        self.assertEqual(self.document.__str__(), "Test Document")
