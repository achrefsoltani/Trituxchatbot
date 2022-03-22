from django.urls import path, include
from .views import (
    ChoiceListApiView,
)

urlpatterns = [
    path('', ChoiceListApiView.as_view()),
    path('<int:id>/', ChoiceListApiView.as_view()),
]
