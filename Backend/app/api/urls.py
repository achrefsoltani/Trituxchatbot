from django.urls import path, include
from .views import (
    ChoiceListApiView,
    ChatApiView,
    MessageApiView
)

urlpatterns = [
    path('chat/', ChatApiView.as_view()),
    path('message/', MessageApiView.as_view()),
    path('', ChoiceListApiView.as_view()),
    path('<int:id>/', ChoiceListApiView.as_view()),

]
