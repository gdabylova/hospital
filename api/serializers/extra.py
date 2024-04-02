from rest_framework import serializers
from api.models import Specialization, Visit, Service


class SpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class ServiceListSerializer(serializers.Serializer):
    name = serializers.CharField()
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)

class ServiceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['cost', 'doctor']

class VisitListSerializer(serializers.Serializer):
    visit_date = serializers.DateTimeField()
    patient = serializers.CharField()
    doctor = serializers.CharField()
    service = serializers.CharField()

class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['doctor', 'status']