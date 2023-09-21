from django.contrib import admin
from django.urls import include, path
from api.views import YourFileView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
    path("uploads/<str:file_name>", YourFileView.as_view(), name="file-view"),
]
