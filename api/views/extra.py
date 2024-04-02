from rest_framework import viewsets, generics
from rest_framework import mixins
from api.models import Service, Visit, Specialization
from api.serializers.extra import ServiceRetrieveSerializer, ServiceListSerializer, ServiceCreateSerializer, \
    ServiceUpdateSerializer, VisitRetrieveSerializer, VisitListSerializer, VisitCreateSerializer, VisitUpdateSerializer, \
    SpecSerializer


class SpecListCreateView(generics.ListCreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecSerializer


class ServiceView(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin
    ):
    lookup_field = 'id'
    def get_serializer_class(self):
        if self.action =='retrieve':
            return ServiceRetrieveSerializer
        if self.action =='list':
            return ServiceListSerializer
        if self.action =='create':
            return ServiceCreateSerializer
        if self.action =='update':
            return ServiceUpdateSerializer
        if self.action =='destroy':
            return ServiceUpdateSerializer

    def get_queryset(self):
        return Service.objects.all()

class VisitView(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin
    ):
    lookup_field = 'id'
    def get_serializer_class(self):
        if self.action =='retrieve':
            return VisitRetrieveSerializer
        if self.action =='list':
            return VisitListSerializer
        if self.action =='create':
            return VisitCreateSerializer
        if self.action =='update':
            return VisitUpdateSerializer
        if self.action =='destroy':
            return VisitUpdateSerializer

    def get_queryset(self):
        return Visit.objects.all()