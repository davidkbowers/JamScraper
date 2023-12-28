from django.urls import path
from health import health_check  # Import the view

urlpatterns = [
    path('', health_check, name='health_check'),
]
