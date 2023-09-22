from django.contrib import admin
from .models import File, TextDocument


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "file_name", "uploaded_at", "processed")
    readonly_fields = ("file_name", "uploaded_at", "processed")
    search_fields = ["file"]

    def file_name(self, obj):
        return obj.file.name.split("/")[-1]  # Возвращает только имя файла без пути

    file_name.short_description = "Загруженный файл"  # Задайте желаемое имя столбца


@admin.register(TextDocument)
class TextDocumentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )
    search_fields = ["title"]
