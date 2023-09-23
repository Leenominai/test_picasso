from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)

from .serializers import (
    FileSerializer,
    BadRequestErrorSerializer,
    NotFoundErrorSerializer,
    InternalServerErrorSerializer,
)


files_view_set_schema = extend_schema_view(
    retrieve=extend_schema(
        request=FileSerializer(many=True),
        summary="Позволяет посмотреть список всех загруженных файлов",
        description="Этот метод позволяет посмотреть список всех загруженных файлов.",
        # responses={
        #     200: OpenApiResponse(
        #         description="OK",
        #     ),
        #     400: OpenApiResponse(
        #         response=BadRequestErrorSerializer,
        #         description="Error: Bad Request",
        #     ),
        #     404: OpenApiResponse(
        #         response=NotFoundErrorSerializer,
        #         description="Error: Not Found",
        #     ),
        #     500: OpenApiResponse(
        #         response=InternalServerErrorSerializer,
        #         description="Error: Internal server error",
        #     ),
        # },
    ),
)
