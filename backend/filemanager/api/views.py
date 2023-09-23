import os

from django.views import View
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.http import FileResponse
from drf_spectacular.utils import extend_schema
from files.models import File
from .serializers import FileSerializer
from .tasks import process_uploaded_file
from .decorators import files_view_set_schema


@extend_schema(tags=["Просмотр списка файлов"])
@files_view_set_schema
class FileListView(generics.ListCreateAPIView):
    """
    Этот метод позволяет посмотреть список всех загруженных файлов.

    - `GET`: Возвращает список всех файлов.
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer
    http_method_names = ["get"]


@extend_schema(tags=["Просмотр деталей файла"])
class FileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детали файла, обновление и удаление.

    - `GET`: Возвращает информацию о файле.
    - `PUT`: Обновляет информацию о файле.
    - `DELETE`: Удаляет файл.
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileUploadView(APIView):
    """
    Загрузка файла.

    - `POST`: Принимает POST-запросы для загрузки файлов. После успешной загрузки файла,
      запускает асинхронную задачу для его обработки с использованием Celery и возвращает
      статус 201 Created и сериализованные данные файла.

    Примечание:
    При загрузке файла выполняется его асинхронная обработка, и результат будет доступен позже.
    """

    def post(self, request, format=None):
        uploaded_files = request.FILES.getlist("file")

        if not uploaded_files:
            return Response({"error": "No files were uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        serialized_data = []

        for uploaded_file in uploaded_files:
            if uploaded_file and uploaded_file.size <= settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
                serializer = FileSerializer(data={"file": uploaded_file})

                if serializer.is_valid():
                    file_instance = serializer.save()

                    process_uploaded_file.delay(file_instance.id)

                    serialized_data.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    {
                        "error": f"File size exceeds the maximum allowed size "
                        f"({settings.FILE_UPLOAD_MAX_MEMORY_SIZE} bytes)"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(serialized_data, status=status.HTTP_201_CREATED)


class YourFileView(View):
    """
    Просмотр файла.

    Этот класс предоставляет способ просмотра файла по его имени. Клиентский код
    может отправить GET-запрос с именем файла на путь /uploads/'имя', и этот класс найдет соответствующий файл
    в медиа-хранилище и отправит его в ответе.

    - `GET`: Возвращает запрошенный файл в ответе.

    Примечание:
    Этот класс полезен для просмотра файлов, загруженных на сервер, и может использоваться,
    например, для просмотра изображений, документов и других типов файлов.
    """

    def get(self, request, file_name):
        file_path = os.path.join(settings.MEDIA_ROOT, "uploads", file_name)

        response = FileResponse(open(file_path, "rb"))
        return response
