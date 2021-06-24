from datetime import datetime
from collections import defaultdict
from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.decorators import api_view, action
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.validators import ValidationError
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserSerializerWithToken, DoctorSerializer, PatientSerializer, VisitSerializer,\
    ChangePasswordSerializer, ToothSerializer, PatientNoteSerializer
from .models import Doctor, Patient, Schedule, Visit, Facility, Tooth, PatientNote


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        user_serializer = UserSerializerWithToken(data=request.data['user'])

        if user_serializer.is_valid():
            user_serializer.save()
            facility = Facility.objects.create(**request.data['facility'])
            Doctor.objects.create(**request.data['doctor'], user_id=user_serializer.data['id'], facility=facility)

            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorsHours(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        hours = defaultdict(list)
        date = request.query_params.get('date')
        facility = request.user.doctor.facility
        schedules = Schedule.objects.filter(doctor__facility=facility, date=date)
        schedules = schedules.exclude(doctor__visit__start_time=F('start_time'), doctor__visit__date=date)
        for schedule in schedules:
            time = schedule.start_time.strftime("%H:%M") + '-' + schedule.end_time.strftime("%H:%M")
            hours[schedule.doctor.id].append(time)
        return Response(hours)

    def post(self, request):
        hour_from = request.query_params.get('hour_from')
        hour_to = request.query_params.get('hour_to')
        date = request.query_params.get('date')
        if hour_from > hour_to:
            raise ValidationError("Godzina od nie może byc późniejsza niż godzina do")
        hours = []
        h_from, m_from = hour_from.split(":")
        h_to, m_to = hour_to.split(":")
        duration = int(h_to) - int(h_from)

        for hour in range(int(h_from), int(h_from)+duration+1):

            if hour != int(h_from) or m_from == '00':
                if int(hour) < 10:
                    hours.append("0%s:00" % hour)
                else:
                    hours.append("%s:00" % hour)
            if hour != int(h_to) or m_to == "30":
                if int(hour) < 10:
                    hours.append("0%s:30" % hour)
                else:
                    hours.append("%s:30" % hour)
        doctor = request.user.doctor
        Schedule.objects.filter(doctor=doctor, date=date).delete()
        for i, hour in enumerate(hours):
            if i != len(hours) - 1:
                Schedule.objects.get_or_create(start_time=hour, end_time=hours[i+1], doctor=doctor, date=date)
        return Response(status=200)


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        facility = self.request.user.doctor.facility
        return Doctor.objects.filter(facility=facility)


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        facility = self.request.user.doctor.facility
        return Patient.objects.filter(facility=facility)


class VisitViewSet(viewsets.ModelViewSet):
    serializer_class = VisitSerializer
    permission_classes = (AllowAny, )
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("patient",)

    def get_queryset(self):
        facility = self.request.user.doctor.facility
        return Visit.objects.filter(doctor__facility=facility)

    @action(detail=False, methods=['GET'])
    def my_visits(self, request):
        visits = Visit.objects.filter(doctor=request.user.doctor, date=datetime.today())
        serializer = self.get_serializer(visits, many=True)

        return Response(serializer.data)


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)


class DoctorSchedule(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        doctor = request.user.doctor
        schedules = Schedule.objects.filter(doctor=doctor, date__gte=date_from,
                                            date__lte=date_to).order_by('date', 'start_time')
        hours = defaultdict(list)
        for schedule in schedules:
            if not hours[str(schedule.date)]:
                hours[str(schedule.date)] = {"start": schedule.start_time, "end": schedule.end_time}
            else:
                hours[str(schedule.date)]["end"] = schedule.end_time
        return Response(hours)


class ToothViewSet(viewsets.ModelViewSet):
    serializer_class = ToothSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("patient",)

    def get_queryset(self):
        facility = self.request.user.doctor.facility
        return Tooth.objects.filter(patient__facility=facility)


class PatientNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PatientNoteSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("patient",)

    def get_queryset(self):
        facility = self.request.user.doctor.facility
        return PatientNote.objects.filter(patient__facility=facility)

