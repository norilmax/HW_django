from django.urls import path
from . import views  # Импортируем views из текущего приложения

urlpatterns = [
    # Маршрут для обработки запросов вида /omlet/, /pasta/ и т.д.
    path('<str:dish>/', views.recipe_view, name='recipe'),
]