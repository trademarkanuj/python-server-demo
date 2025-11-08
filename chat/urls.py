from django.urls import path
from .views import ChatView
urlpatterns=[ path("messages/",ChatView.as_view()) ]
