from django.contrib import admin
from django.urls import path, include
from .views import home, api_test

urlpatterns = [
    path("", home),
    path("api/", api_test),
    path("api/chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
]
