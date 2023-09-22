import os

from django.views import View
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileSerializer
from .tasks import process_uploaded_file
from files.models import File
from django.conf import settings
from django.http import FileResponse


class FileList(generics.ListCreateAPIView):
    """
    Список файлов и создание новых файлов.

    - `GET`: Возвращает список всех файлов.
    - `POST`: Создает новый файл. При успешной загрузке файла, запускается асинхронная задача
      для его обработки с использованием Celery.
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer
    http_method_names = ['get']


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Детали файла, обновление и удаление.

    - `GET`: Возвращает информацию о файле.
    - `PUT`: Обновляет информацию о файле.
    - `DELETE`: Удаляет файл.
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileUpload(APIView):
    """
    Загрузка файла.

    - `POST`: Принимает POST-запросы для загрузки файлов. После успешной загрузки файла,
      запускает асинхронную задачу для его обработки с использованием Celery и возвращает
      статус 201 Created и сериализованные данные файла.
    """

    def post(self, request, format=None):
        uploaded_file = request.FILES.get("file")

        if uploaded_file and uploaded_file.size <= settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
            serializer = FileSerializer(data=request.data)
            if serializer.is_valid():
                # Сохраните файл на сервере
                file_instance = serializer.save()

                # Запустите асинхронную задачу для обработки файла с использованием Celery
                process_uploaded_file.delay(file_instance.id)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"error": f"File size exceeds the maximum allowed size ({settings.FILE_UPLOAD_MAX_MEMORY_SIZE} bytes)"},
                status=status.HTTP_400_BAD_REQUEST
            )


class YourFileView(View):
    def get(self, request, file_name):
        # Постройте путь к файлу на основе имени файла
        file_path = os.path.join(settings.MEDIA_ROOT, "uploads", file_name)

        # Отправьте файл в ответе
        response = FileResponse(open(file_path, "rb"))
        return response
