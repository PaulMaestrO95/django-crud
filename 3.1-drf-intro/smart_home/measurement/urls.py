from django.urls import path
from measurement.views import SensorsView, MeasurementView, SingleSensorView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SingleSensorView.as_view()),
]