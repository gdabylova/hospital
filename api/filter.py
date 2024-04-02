import django_filters as filters

from api.models import Doctor, Patient


class DoctorFilterSet(filters.FilterSet):
    last_name = filters.CharFilter(field_name='last_name')

    class Meta:
        model = Doctor
        fields = {
            'last_name': ['exact', 'icontains'],
            'first_name': ['exact'],
            'specialization': ['exact']
        }

class PatientFilterSet(filters.FilterSet):
    gender = filters.CharFilter(field_name='gender')

    class Meta:
        model = Patient
        fields = {
            'gender': ['exact', 'icontains'],
        }
