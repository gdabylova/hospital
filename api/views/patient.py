from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from api.filter import PatientFilterSet
from api.mixin import HospitalGenericViewSet
from api.models import Patient, Doctor

from api.serializers.patient import PatientListSerializer, PatientRetrieveSerializer, PatientUpdateSerializer, PatientCreateSerializer


class PatientView(
    HospitalGenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['gender']
    filterset_class = PatientFilterSet
    search_fields = ['first_name', 'last_name']


    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_patient', ]
        elif self.action == 'create':
            self.action_permissions = ['add_patient']
        elif self.action == 'update':
            self.action_permissions = ['change_patient']
        elif self.action == 'destroy':
            self.action_permissions = ['delete_patient']



    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PatientRetrieveSerializer
        if self.action == 'list':
            return PatientListSerializer
        if self.action == 'create':
            return PatientCreateSerializer
        if self.action == 'update':
            return PatientUpdateSerializer
        if self.action == 'destroy':
            return PatientRetrieveSerializer


    def get_queryset(self):
        return Patient.objects.all()



