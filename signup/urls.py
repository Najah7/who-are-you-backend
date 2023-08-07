from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserCreate.as_view(), name="create_user"),
]