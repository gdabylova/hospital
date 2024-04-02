from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.response import Response
from ..filter import DoctorFilterSet
from ..mixin import HospitalGenericViewSet
from ..models import Patient, Doctor
from ..serializers.doctor import DoctorRetrieveSerializer, DoctorListSerializer, DoctorCreateSerializer, \
    DoctorUpdateSerializer
from ..serializers.patient import PatientListSerializer


class DoctorView(
    HospitalGenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin
    ):
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['first_name', 'last_name', 'specialization']
    filterset_class = DoctorFilterSet

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_doctor',]
        elif self.action == 'list_patient':
            self.action_permissions = ['view_patient']
        else:
            self.action_permissions = []

    def get_serializer_class(self):
        # print("Action:", self.action)
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer
        if self.action == 'destroy':
            return DoctorRetrieveSerializer
        # print("No serializer for action:", self.action)
        return None

    def get_queryset(self):
        if self.action =='list_patient':
            return Patient.objects.all()
        return Doctor.objects.all()

    def list_patient(self, request, id):
        queryset = self.get_queryset().filter(visits__doctor_id=id).all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
