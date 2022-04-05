from django.urls import path, include
from .views import (
    ChoiceListApiView,
    ChatApiView,
    MessageApiView
)

urlpatterns = [
    path('chat/', ChatApiView.as_view()),
    path('message/', MessageApiView.as_view()),
    path('choices/', ChoiceListApiView.as_view()),
    path('choices/<int:id>/', ChoiceListApiView.as_view()),

]
