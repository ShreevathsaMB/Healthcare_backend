from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, MyTokenObtainPairView, DoctorViewSet, PatientViewSet, MappingViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register('doctors', DoctorViewSet, basename='doctors')
router.register('patients', PatientViewSet, basename='patients')
router.register('mappings', MappingViewSet, basename='mappings')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]