from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_resume, name="upload_resume"),
    path("fill-missing/<int:pk>/", views.fill_missing_fields, name="fill_missing_fields"),
]
