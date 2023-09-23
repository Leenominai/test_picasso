from rest_framework import serializers
from files.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("file", "uploaded_at", "processed")

    # Добавьте это поле для предоставления URL без /media/
    def to_representation(self, instance):
        ret = super().to_representation(instance)

        file_url = instance.file.url
        ret["file"] = file_url.replace("/media/", "/")

        return ret


class BadRequestErrorSerializer(serializers.Serializer):
    detail = serializers.CharField(
        default="BadRequest.",
        help_text="Сообщение об ошибке",
    )


class NotFoundErrorSerializer(serializers.Serializer):
    detail = serializers.CharField(
        default="Not found.",
        help_text="Сообщение об ошибке",
    )


class InternalServerErrorSerializer(serializers.Serializer):
    detail = serializers.CharField(
        default="Internal server error.",
        help_text="Сообщение об ошибке",
    )
