from django.db import models


class File(models.Model):
    """
    Модель для представления загруженных файлов.

    Поля:
    - file: Поле типа FileField для загрузки файла.
    - uploaded_at: Поле типа DateTimeField, которое автоматически устанавливает
                   дату и время загрузки файла при создании записи.
    - processed: Поле типа BooleanField, указывающее, был ли файл обработан.
                 По умолчанию устанавливается в False.
    """

    file = models.FileField(upload_to="uploads/", verbose_name="Загруженный файл")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время загрузки")
    processed = models.BooleanField(default=False, verbose_name="Файл обработан")

    def __str__(self):
        return self.file.name


class TextDocument(models.Model):
    """
    Модель для хранения текстовых документов с указанием заголовка и содержимого.

    Поля:
    - title: Поле типа CharField для хранения заголовка документа.
    - content: Поле типа TextField для хранения содержимого документа.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
