from rest_framework import serializers
from files.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("file", "uploaded_at", "processed")

    # Добавьте это поле для предоставления URL без /media/
    def to_representation(self, instance):
        ret = super().to_representation(instance)

        # Получите абсолютный URL для файла и замените '/media/' на '/'
        file_url = instance.file.url
        ret["file"] = file_url.replace("/media/", "/")

        return ret
