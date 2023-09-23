from django.contrib import admin
from .models import File, TextDocument


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели File.

    - `list_display`: Определяет, какие поля будут отображаться в списке объектов модели в административной панели.
    - `readonly_fields`: Задает поля, которые будут доступны только для чтения и не могут быть изменены администратором.
    - `search_fields`: Позволяет выполнять поиск объектов по указанным полям.
    """

    list_display = ("id", "file_name", "uploaded_at", "processed")
    readonly_fields = ("file_name", "uploaded_at", "processed")
    search_fields = ["file"]

    def file_name(self, obj):
        """
        Получить имя файла.
        """
        return obj.file.name.split("/")[-1]

    file_name.short_description = "Загруженный файл"


@admin.register(TextDocument)
class TextDocumentAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели TextDocument.

    """

    list_display = (
        "id",
        "title",
    )
    search_fields = ["title"]
