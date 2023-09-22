from django.urls import path
from .views import FileList, FileDetail, FileUpload


urlpatterns = [
    path("files/", FileList.as_view(), name="file-list"),
    path("files/<int:pk>/", FileDetail.as_view(), name="file-detail"),
    path("upload/", FileUpload.as_view(), name="file-upload"),
]
