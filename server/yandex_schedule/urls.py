from django.urls import path
from .views import YandexAPIView

urlpatterns = [
    path('yandex/', YandexAPIView.as_view()),
]
