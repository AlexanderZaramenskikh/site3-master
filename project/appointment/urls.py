from django.urls import path
from .views import AppointmentView

urlpatterns = [
    path('appoin', AppointmentView.as_view()),
]