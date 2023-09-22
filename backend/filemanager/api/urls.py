from django.urls import path
from .views import FileListView, FileDetailView, FileUploadView


urlpatterns = [
    path("files/", FileListView.as_view(), name="file-list"),
    path("files/<int:pk>/", FileDetailView.as_view(), name="file-detail"),
    path("upload/", FileUploadView.as_view(), name="file-upload"),
]
