from rest_framework import serializers

from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id_sensor', 'temperature', 'date']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['name', 'description']


class ScanerMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date']


class SensorDetailedSerializer(serializers.ModelSerializer):
    measurements = ScanerMeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['name', 'description', 'measurements']
