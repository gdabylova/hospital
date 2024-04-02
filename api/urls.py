from django.urls import path
# from rest_framework.authtoken import views - для простого токена
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import DoctorView, PatientView
from api.views.extra import ServiceView, VisitView, SpecListCreateView

urlpatterns = [

    path('specialization/', SpecListCreateView.as_view()),
    path('doctor/', DoctorView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('doctor/<int:id>', DoctorView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('doctor/<int:id>/patient/', DoctorView.as_view({
        'get': 'list_patient',

    })),

    path('patient/', PatientView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('patient/<int:id>', PatientView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    path('service/', ServiceView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('service/<int:id>', ServiceView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('visit/', VisitView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('visit/<int:id>', VisitView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    # path('token/', views.obtain_auth_token), простой токен
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]