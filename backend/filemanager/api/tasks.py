from __future__ import absolute_import, unicode_literals

import os
import fitz

from celery import shared_task
from PIL import Image
from django.conf import settings
import mimetypes
from files.models import File, TextDocument


def process_pdf(file_path, file_instance):
    pdf_document = fitz.open(file_path)
    text = ""
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        text += page.get_text()
    pdf_document.close()
    file_name = os.path.basename(file_instance.file.name)
    text_document = TextDocument(title=file_name, content=text)
    text_document.save()
    return text_document


@shared_task
def process_uploaded_file(file_id):
    try:
        file_instance = File.objects.get(pk=file_id)

        file_path = settings.MEDIA_ROOT / file_instance.file.name

        mime_type, _ = mimetypes.guess_type(file_path)

        if mime_type is None:
            # Попробуем определить MIME-тип на основе расширения файла
            file_extension = os.path.splitext(file_path)[1].lower()
            mime_type = mimetypes.types_map.get(file_extension, None)

        print(f"MIME Type: {mime_type}")

        if mime_type and mime_type.startswith("image"):
            # Если это изображение, измените его размер на 300x300
            image = Image.open(file_path)
            image.thumbnail((300, 300))
            image.save(file_path)

        elif mime_type == "application/pdf":
            text_document = process_pdf(file_path, file_instance)
            print(f"Processed PDF: {text_document.title}")

        elif mime_type == "text/plain":
            # Обработка текстовых файлов
            with open(file_path, "r") as text_file:
                text = text_file.read()

            file_name = os.path.basename(file_instance.file.name)
            text_document = TextDocument(title=file_name, content=text)
            text_document.save()
            print(f"Processed text file: {file_instance.file.name}")

        else:
            print(f"Unsupported MIME Type: {mime_type}")

        file_instance.processed = True
        file_instance.save()

    except File.DoesNotExist:
        pass
