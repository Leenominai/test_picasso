from __future__ import absolute_import, unicode_literals

from celery import shared_task
from PIL import Image
from django.conf import settings
import mimetypes
from files.models import File


@shared_task
def process_uploaded_file(file_id):
    try:
        file_instance = File.objects.get(pk=file_id)

        file_path = settings.MEDIA_ROOT / file_instance.file.name

        mime_type, _ = mimetypes.guess_type(file_path)

        if mime_type.startswith('image'):
            # Если это изображение, измените его размер на 300x300
            image = Image.open(file_path)
            image.thumbnail((300, 300))
            image.save(file_path)

        file_instance.processed = True
        file_instance.save()

    except File.DoesNotExist:
        pass
