from django.urls import path, include
from .views import current_user, UserList, DoctorViewSet, PatientViewSet, DoctorsHours, VisitViewSet, \
    ChangePasswordView, DoctorSchedule, ToothViewSet, PatientNoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'patient-notes', PatientNoteViewSet, basename='patient-notes')
router.register(r'visits', VisitViewSet, basename='visits')
router.register(r'teeth', ToothViewSet, basename='teeth')

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('doctors_hours/', DoctorsHours.as_view()),
    path('doctors_schedule/', DoctorSchedule.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('', include(router.urls))
]