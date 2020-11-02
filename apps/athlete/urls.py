from django.urls import path

from apps.athlete.views import FileUploadAPIView

urlpatterns = [
    path('upload/', FileUploadAPIView.as_view())
]
