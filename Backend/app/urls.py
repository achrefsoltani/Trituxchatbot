
from django.urls import path, include

import app.views

urlpatterns = [
    path('api/', include('app.api.urls')),
]
