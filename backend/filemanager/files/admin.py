from django.contrib import admin
from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    """
    Отображение модели Files в Админке.
    """

    list_display = ("file", "uploaded_at", "processed")
    list_filter = ("processed",)
    search_fields = ("file",)
