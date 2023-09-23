from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .views import FileListView, FileDetailView, FileUploadView


urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("files/", FileListView.as_view(), name="file-list"),
    path("files/<int:pk>/", FileDetailView.as_view(), name="file-detail"),
    path("upload/", FileUploadView.as_view(), name="file-upload"),
]
